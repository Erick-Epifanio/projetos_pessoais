import math
import os


def Insert_data():
    run = True
    while run:
        try:
            a = float(int(input("A: "))) or 0
            b = float(int(input("B: "))) or 0
            c = float(int(input("C: "))) or 0

            if input(f"\nValores inseridos:\n| {a}\n| {b}\n| {c}\n\nDeseja continuar ou refazer? S/N: ").upper() == "S":
                run = False
                return a, b, c
            else:
                raise Exception("resetando....")
        except Exception:
            os.system("cls")
        except ValueError:
            os.system("cls")
            print("Erro de inserção")

def Equal_Delta(a, b, c):
    Delta = pow(b, 2) - 4 * a * c
    return Delta

def Equal_geral(a, b, c, Delta):
    pass

a, b, c = Insert_data()

print(Equal_Delta(a,b,c))