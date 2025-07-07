import json
import random
import os

package = {}

file_name = str(input("nome do arquivo .json (não precisa colocar a extensão do aquivo, é automatico!\n/> "))

test_file =  file_name + ".json"

if os.path.exists(test_file):
    
    print(f"{file_name} existente.")
    if input("deseja reescreve-lo? s/n: ").upper() == "S":
        file_name = file_name + ".json"
    else:
        file_name = file_name + str(random.randint(1, 100)) + ".json"
else:
    file_name = file_name + ".json"
    
print(f"\n\nSeu arquivo é ---> {file_name}")


class System_json:
    def __init__(self, File_name, Data):
        self.File = File_name
        self.Data = Data
    
    def READ_json(self):
        with open(self.File, "r") as FILE:
            loading = json.load(FILE)
            print("+","-"*25,"+")
            for KEY, DATA  in loading.items():
                print(f"| {KEY} -- {DATA}")
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
        if input("\narquivo pronto :D, quer ver-lo? S/N ").upper() == "S":
            main.READ_json()
            running = False
        else:
            running = False

    except FileNotFoundError:
        print(0)
        running = False