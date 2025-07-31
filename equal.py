import math
import os


def Insert_data():
    run = True
    while run:
        try:
            a = float(int(input(" A: "))) or 1
            b = float(int(input(" B: "))) or 1
            c = float(int(input(" C: "))) or 1

            if input(f"\n Valores inseridos:\n| {a}\n| {b}\n| {c}\n\n Deseja continuar ou refazer? S/N: ").upper() == "S":
                run = False
                return a, b, c
            else:
                raise Exception(" resetando....")
        except Exception:
            os.system("clear")
        except ValueError:
            os.system("clear")
            print("Erro de inserção")

def Equal_Delta(a, b, c):
    Delta = pow(b, 2) - 4 * a * c
    return Delta

def Equal_geral(a, b, c, Delta):
    
    def x_mais():
        x1 = (-1*b) + math.sqrt(Delta)
        x1 = x1 / (2 * a)
        return x1
        
    def x_menos():
        x2 = (-1*b) - math.sqrt(Delta)
        x2 = x2 / (2 * a)
        return x2
    x1 = x_mais()
    x2 = x_menos()   
    print(f"x': {x1}")
    print(f'x": {x2}')


while True:
    input("Pressione Enter para continuar...")
    os.system("clear")
    a, b, c = Insert_data()
    Delta = Equal_Delta(a, b, c)
    Equal_geral(a, b, c, Delta)