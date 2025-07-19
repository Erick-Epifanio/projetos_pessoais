import json
from time import sleep



# input para preencher

lista = {}


def entry():
    print("insira os dados [key-data]. para sair aperte 'Enter'.")
    run = True
    while True:
        try:
            Key_data = input("KEY-DATA> ") or None #entrada de dados segundo a regra de separação por -

            if not Key_data == None:
                Key_data = Key_data.split('-') #divide os dados em dois [chave | dado]
                lista[Key_data[0]] = Key_data[1]   # chave = dado /dicionário
                

            elif Key_data == None:
                print("Saindo da digitação de entrada.....")
                sleep(2)
                break

            else:
                continue

        #tratamentos de erros
        except ValueError: 
            print("Erro de digitação!")
            pass

        except IndexError:
            print("Erro de digitação!")
            pass



# verifição de arquivo .json

try:
    print("verificando a existencia do arquivo 'dados.json'....")
    sleep(2)
    with open("dados.json", 'r') as File:
        print("Arquivo existe!\n\nPreparando processo....\n")
        retorno = json.load(File)
        
        for key, data in retorno.items():
            print(f'{key} --- {data}')

    with open("dados.json", 'w') as File:
        if input("Modificar? S/N: ").upper() == "S":
            entry()
        json.dump(lista, fp=File, indent=4)
        for key, data in retorno.items():
            print(f'{key} --- {data}')

        
        
except FileNotFoundError:
    with open("dados.json", 'w') as File:
        print("arquivo não encontrado :(\nPreparando arquivo...")
        sleep(2)
        print("Arquivo criado com sucesso :)\nPassando a limpo os dados do dicionário para o arquivo JSON....")
        entry()
        json.dump(lista, fp=File, indent=4)

