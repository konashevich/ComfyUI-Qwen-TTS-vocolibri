$root = Resolve-Path (Join-Path $PSScriptRoot "..")
$soxPath = Join-Path $env:LOCALAPPDATA "Microsoft\WinGet\Packages\ChrisBagwell.SoX_Microsoft.Winget.Source_8wekyb3d8bbwe\sox-14.4.2"
$env:PATH = "$soxPath;$env:PATH"
& (Join-Path $root ".venv\Scripts\python.exe") (Join-Path $root "ComfyUI\main.py") --listen 0.0.0.0 --port 8188
