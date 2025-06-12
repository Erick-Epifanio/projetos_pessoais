import pandas as pd



class entrada:
    def __init__(self):
        self.coll1 = input(">")               #colunas
        self.data = input(">").split(",")     #dados por linha
    
    def construc(self):
        dic = {self.coll1 : self.data}        #relação de coluna e dado
        Df = pd.DataFrame(dic)
        print(Df)

entry = None
for _ in range(11):
    entry += entrada()


entry.construc()

#estou terminando  T_ T

