#questão 1

# 1h ---> 60m     x3600
# 1m ---> 60s     x60
# 1s ---> 1000    x1000


def past(h, m, s):
    Ss = 0

    # verificando as horas e convertendo para segundos
    if 0 <= h <= 23:
        Ss += h*3600
    else:
        Ss += 0
    
    #verificando os minutos e convertendo para segundos
    if 0 <= m <= 59:
        Ss += m*60
    else:
        Ss += 0

    #verificando os segundos

    if 0 <= s <= 59:
        Ss += s
    else:
        Ss += 0

    return Ss*1000

    