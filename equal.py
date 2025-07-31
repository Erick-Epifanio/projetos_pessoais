import math
import os
import termcolor


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
                raise Exception(termcolor.colored(" resetando....", "yellow"))
        except Exception:
            os.system("cls")
        except ValueError:
            os.system("cls")
            print("Erro de inserção")

def Equal_Delta(a, b, c):
    Delta = pow(b, 2) - 4 * a * c
    return Delta

def Equal_geral(a, b, c, Delta):
    
    def x_mais():
        try:
            x1 = (-1*b) + math.sqrt(Delta)
            x1 = x1 / (2 * a)
            return x1
        except ValueError:
            print(termcolor.colored(f"Erro de operação envolvendo 'Raiz quadrada' com {Delta}", "yellow"))
            return termcolor.colored("XXXX", "red")
        
    def x_menos():
        try:
            x2 = (-1*b) - math.sqrt(Delta)
            x2 = x2 / (2 * a)
            return x2
        except ValueError:
            print(termcolor.colored(f"Erro de operação envolvendo 'Raiz quadrada' com {Delta}", "yellow"))
            return termcolor.colored("XXXX", "red")
        
    x1 = x_mais()
    x2 = x_menos()   
    print(f"x': {x1}")
    print(f'x": {x2}')


while True:
    input("Pressione Enter para continuar...")
    os.system("cls")
    a, b, c = Insert_data()
    Delta = Equal_Delta(a, b, c)
    Equal_geral(a, b, c, Delta)