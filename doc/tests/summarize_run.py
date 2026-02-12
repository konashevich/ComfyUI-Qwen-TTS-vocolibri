#!/usr/bin/env python
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass
class RunStats:
    log_path: Path
    start: datetime | None
    end: datetime | None
    wall: str | None
    batches: int
    avg_batch_s: float | None
    p50_batch_s: float | None
    min_batch_s: float | None
    max_batch_s: float | None
    parts: int
    full_wav_exists: bool
    full_wav_size_mb: float | None
    done: bool


def parse_stats(output_dir: Path) -> RunStats:
    log_path = output_dir / "run.log"
    text = log_path.read_text(errors="ignore") if log_path.exists() else ""

    ts = re.findall(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),\d{3} - ", text, flags=re.M)
    start = datetime.strptime(ts[0], "%Y-%m-%d %H:%M:%S") if ts else None
    end = datetime.strptime(ts[-1], "%Y-%m-%d %H:%M:%S") if len(ts) >= 2 else None
    wall = str(end - start) if start and end else None

    batch_s = [float(x) for x in re.findall(r"Batch completed in ([0-9]+\.[0-9]+)s", text)]
    if batch_s:
        batch_s_sorted = sorted(batch_s)
        batches = len(batch_s_sorted)
        avg = sum(batch_s_sorted) / batches
        p50 = batch_s_sorted[batches // 2] if batches % 2 == 1 else (batch_s_sorted[batches // 2 - 1] + batch_s_sorted[batches // 2]) / 2
        mn = batch_s_sorted[0]
        mx = batch_s_sorted[-1]
    else:
        batches = 0
        avg = p50 = mn = mx = None

    parts = len(list(output_dir.glob("part_*.wav")))
    full_wav = output_dir / "full_audiobook.wav"
    full_exists = full_wav.exists()
    full_size_mb = (full_wav.stat().st_size / (1024 * 1024)) if full_exists else None

    done = " - INFO - Done." in text

    return RunStats(
        log_path=log_path,
        start=start,
        end=end,
        wall=wall,
        batches=batches,
        avg_batch_s=avg,
        p50_batch_s=p50,
        min_batch_s=mn,
        max_batch_s=mx,
        parts=parts,
        full_wav_exists=full_exists,
        full_wav_size_mb=full_size_mb,
        done=done,
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("output_dir", type=Path)
    args = ap.parse_args()

    stats = parse_stats(args.output_dir)
    print(f"Output dir: {args.output_dir}")
    print(f"Log      : {stats.log_path} ({'exists' if stats.log_path.exists() else 'missing'})")
    if stats.start:
        print(f"Start    : {stats.start}")
    if stats.end:
        print(f"End      : {stats.end}")
    if stats.wall:
        print(f"Wall     : {stats.wall}")
    print(f"Parts    : {stats.parts}")
    print(f"Full wav : {'yes' if stats.full_wav_exists else 'no'}" + (f" ({stats.full_wav_size_mb:.1f} MB)" if stats.full_wav_size_mb is not None else ""))
    print(f"Done     : {'yes' if stats.done else 'no'}")
    print(f"Batches  : {stats.batches}")
    if stats.batches and stats.avg_batch_s is not None:
        print(
            "Batch s  : "
            f"avg={stats.avg_batch_s:.2f} "
            f"p50={stats.p50_batch_s:.2f} "
            f"min={stats.min_batch_s:.2f} "
            f"max={stats.max_batch_s:.2f}"
        )


if __name__ == "__main__":
    main()
