import pandas as pd
import os

if os.path.exists("teste.csv"):
    print("arquivo encontrado!")
elif not os.path.exists("teste.csv"):
    print("crindo arquivos.")
    file = open("teste.csv", "+a")
    file.close()
        


class entrada:
    def __init__(self, column, data):
        self.column = column
        self.data = data
        self.dataframe = pd.DataFrame()

    def construct(self):
        self.dataframe[self.column] = self.data
    def screen(self):
        self.dataframe.to_csv("teste.csv", index=False)
        print(self.dataframe)


while True:
    column = input('column name> ')
    data = input("dados> ").split(",")
    entry = entrada(column, data)
    
    if input('terminar registro? S/N: ').upper() == "S":
        break
    else:
        continue

entry.construct()
entry.screen()



#estou terminando  T_ T

