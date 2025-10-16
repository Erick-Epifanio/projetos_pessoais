@echo off
REM Limpa a pasta dist e build
rmdir /s /q dist
rmdir /s /q build

REM Compila com PyInstaller (one-folder para evitar _MEI)
pyinstaller --noconsole --clean autoclick_v3.2_.py

xcopy imagens dist\autoclick_v3.2_\imagens /E /Y

rmdir /s /q build
del autoclick_v3.2_.spec

pause