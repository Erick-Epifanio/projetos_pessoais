import os
import random
import json as js


class Main:                            
    def __init__(self, file):
        self.memory_working_temp = {}
        self.file_temp_json = file + "_temp.json"
        self.file_json = file + ".json"


    def Pre_Load(self):
        try:                    # Pré carregamento dos dados de arquivo existentes para serem modificados
            with open(self.file_json, 'r') as file_r:
                load = js.load(file_r)
                self.memory_working_temp.update(load)
        except FileNotFoundError:
            self.memory_working_temp = {}
    
    def write_json(self, data_insert):
        try:
            if os.path.exists(self.file_json):
                self.pre_load()
        except FileNotFoundError:
            pass        
        def increment(data_insert):
            self.Pre_Load()
            self.memory_working_temp.update(data_insert)
            with open(self.file_temp_json, 'w') as file_in:
                js.dump(self.memory_working_temp, file_in, indent=4)
            
        def overwrite(data_insert):
            with open(self.file_json, "w", encoding="utf-8") as file_w:
                js.dump(data_insert, file_w,ensure_ascii=False, indent=4)
        
        print(f"Deseja, incrementar dados ao arquivo {self.file_temp_json}?\nAo salvar o arquivo real, a versão temporário será deletada.")
        if input(f"(s/n)\t> ").upper() == "S":
            increment(data_insert)
            os.system("cls")
        else:
            overwrite(data_insert)
            os.system("cls")
        
        if input(f"Deseja visualizar o conteúdo do {self.file_temp_json} ?\n(s/n): ").lower() == "s":
            print(js.dumps(self.memory_working_temp, indent=4))
            with open(self.file_json, "w", encoding="utf-8") as real_file:
                js.dump(self.memory_working_temp, real_file, ensure_ascii=False, indent=4)
                os.remove(self.file_temp_json)
                print("arquivo temporario deletado com sucesso")
        else:
            with open(self.file_json, "w", encoding= "utf-8") as real_file:
                js.dump(self.memory_working_temp, real_file, ensure_ascii=False, indent=4)
            os.remove(self.file_temp_json)
            print("arquivo temporario deletado com sucesso")

def archive():
    archive_name = str(input("Digite o nome do arquivo, não precisa colocar a extensão.\n/> "))

    if os.path.exists(archive_name + ".json"):
        if input(f"Arquivo {archive_name}.json já existe, Deseja sobrescrever? (s/n)\n\nOBS: Um número aleatório entre 1 a 1000 será atribuído antes da extensão .json caso não queira sobrescrever\n/> ").lower() == "s":
            os.system("cls")
            return archive_name
        else:
            archive_name = archive_name + str(random.randint(1, 1000))
            os.system("cls")
            return archive_name
    else:
        return archive_name

def insert_data():
    run = True
    package = {} 
    while run:
        try:
            data = input("ex: teste-100 ou Ctrl+C para sair: ").split("-")
            os.system("cls")
            if len(data) == 2:
                package[data[0]] = data[1]
                print( js.dumps(package, indent= 4))
                continue
            elif len(data) != 2:
                print("Erro de inserção.")
        except KeyboardInterrupt:
            print("\nSaindo do insersor...")
            run = False
    return package   
master = Main(archive())
master.write_json(insert_data())