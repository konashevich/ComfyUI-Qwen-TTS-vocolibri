import datetime
import pathlib
import sys

input_path = pathlib.Path(r'C:\Users\akona\OneDrive\Dev\Public-VS-Private\Ledger Journal\Ledger-LaTeX-Template-OTH\Debunking_Blockchain_TTS.md')
text = input_path.read_text(encoding='utf-8')
chars = len(text)
words = len(text.split())

out_dir = pathlib.Path('output/Debunking_Blockchain_Male_0.6B')
chunk_paths = sorted(out_dir.glob('part_*.wav'))
if not chunk_paths:
    print('No chunk files found in output directory.')
    sys.exit(1)

start_ts = min(p.stat().st_ctime for p in chunk_paths)
end_ts = max(p.stat().st_mtime for p in chunk_paths)
full_audio = out_dir / 'full_audiobook.wav'
if full_audio.exists():
    end_ts = max(end_ts, full_audio.stat().st_mtime)

start_dt = datetime.datetime.fromtimestamp(start_ts)
end_dt = datetime.datetime.fromtimestamp(end_ts)
duration = end_ts - start_ts
avg_char = duration / chars if chars else float('inf')
avg_word = duration / words if words else float('inf')
cps = chars / duration if duration else float('inf')
wps = words / duration if duration else float('inf')

print('Character count:', chars)
print('Word count:', words)
print('Start:', start_dt.isoformat(' '))
print('End:', end_dt.isoformat(' '))
print('Duration (seconds):', format(duration, '.2f'))
print('Avg seconds/char:', format(avg_char, '.6f'))
print('Avg seconds/word:', format(avg_word, '.6f'))
print('Chars per second:', format(cps, '.2f'))
print('Words per second:', format(wps, '.2f'))
