python -m PyInstaller main.py --onefile -n srpa.exe
rmdir /q /s build
del /f /q /s srpa.exe.spec