import pandas as pd

teste1 = input().split(",")
teste2 = input().split(",")


protologos = {
    "nomes": teste1,
    "idade": teste2,
    None: None
}

DF = pd.DataFrame(protologos)

print(DF)

with pd.ExcelWriter("excel.xlsx") as file:
    DF.to_excel(file, index=False)


