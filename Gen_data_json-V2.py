import json
from time import sleep

package = {}

file_name = str(input("nome do arquivo .json (não precisa colocar a extensão do aquivo, é automatico!\n/> ")) + ".json"


class System_json:
    def __init__(self, File_name, Data):
        self.File = File_name
        self.Data = Data
    
    def READ_json(self):
        with open(self.File, "r") as FILE:
            loading = json.load(FILE)
            print("+","-"*25,"+")
            for KEY, DATA  in loading.items():
                print(f"|{KEY} -- {DATA}")
            print("+","-"*25,"+")

            
    def WRITE_json(self):
        with open(self.File, "w") as FILE:
            json.dump(self.Data, fp=FILE, indent=4)

def treatment():
    run = True
    print("\nRegra: defina a separação do conjunto por meio do '-' (sem espaço entre os dados) \n\nEx: Teste-100\n\nEvite nomear a chave com o nome da anterior enquanto não trabalho nisso.\nPois o dado armazenado será transcrevido pelo valor posterior caso ambas as chaves sejam escritas da mesma forma...\nSe serve de consolo, o script ainda mantem o Case-Sensitive Ex: Teste != teste...\nMas se você persistir nesse erro o problema já não é mais o codigo e sim em você.   (⚆_⚆)")
    while run:
        try:
            entry = input("/>") or None
            Key_And_Data = entry.split("-")
            package[Key_And_Data[0]] = Key_And_Data[1]

        except ValueError:
            continue
        except IndexError:
            continue
        except KeyboardInterrupt:
            print("saindo.....")
            run = False
treatment()

running = True
while running:
    try:
        main = System_json(file_name, package)
        main.WRITE_json()
        main.READ_json()
        print("\narquivo pronto :D")
        running = False

    except FileNotFoundError:
        print(0)
        running = False