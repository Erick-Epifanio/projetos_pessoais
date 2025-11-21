@echo off
:: Limpa a pasta dist e build

echo ================================
if exist dist (
    rmdir /s /q dist
) else (
    echo pass
)
if exist build (
    rmdir /s /q build
) else (
    echo pass
)

echo ================================
:: Compila com PyInstaller (one-folder para evitar _MEI)

if exist autoclick_v3.3_.py (
    pyinstaller --noconsole --clean autoclick_v3.3_.py
) else (
    echo arquivo alvo nao encontrado, certifique de que ele esteja no mesmo diretorio que o Builder
)

if exist build (
    rmdir /s /q build
)

if exist autoclick_v3.3_.spec (
    del autoclick_v3.3_.spec
)

echo ================================
pause