@echo off

python --version

color 06

echo ==================================================
echo            Instalador de requisitos
echo ==================================================

pause

if exist requirement.txt (
    
    echo arquivo de dependencias encontrado, iniciando download.
    echo _________________________________________________________
    color 0A
    pip install -r requirement.txt

) else (
    color 0C
    echo _________________________________________________________
    echo arquivo não encontrado, por favor, verifique a existencia do arquivo.
)

pause