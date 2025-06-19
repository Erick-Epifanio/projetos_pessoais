import pandas as pd
import os

class principal:
    def __init__(self):  #construção de objetos
        self.column = {}
        self.data = []
        self.conjuc = []

    def config_data(self): #configuração das linhas por coluna
        while True:
            self.data.append(input("dados > "))   #adiciona cada dado para a lista self.data
            if input("continuar? S/N: ").upper() == "N":
                break
            else:
                continue

    def config_column(self):
        contagem = len(self.column)
        self.column[f"coluna_{contagem}"] = self.data
    


class add_column(principal):
    def adicionar(self):
        self.data = []
        while True:

            if input("adicionar mais uma coluna? S/N: ").upper() == "S":
                self.config_data()
                self.config_column()
            else:
                df = pd.DataFrame(self.column)
                df.to_csv("construct.csv", index=False)
                print(df)
                break


sets = add_column()  # instância única da subclasse
sets.config_data()
sets.config_column()
sets.adicionar()

