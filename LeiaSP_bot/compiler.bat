@echo off
REM Limpa a pasta dist e build
rmdir /s /q dist
rmdir /s /q build

REM Compila com PyInstaller (one-folder para evitar _MEI)
pyinstaller --noconsole --clean generic_autoclick.py

xcopy imagens dist\generic_autoclick\imagens /E /Y

rmdir /s /q build
del generic_autoclick.spec

pause