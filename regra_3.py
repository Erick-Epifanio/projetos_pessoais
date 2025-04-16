#import os


X = []
Z = []
f=1

#________________________________________LOOP_____________________________________________
print(' X --------\n')
while f<=2:
   X1=input('>')
   X.append(X1)
   f= f+1
   #os.system('cls')
f=1   
print('\n Z --------\n')   
while f<=2:
   Z1=input('>')
   Z.append(Z1)
   f= f+1
   #os.system('cls')



#_____________________________________ TABELA ______________________________________________
   
print(' ')
print('','_'*12)
for item, item1 in zip(X,Z):
   print(' |',item,'---',item1,' |')

print('','-'*12)
print(' ')


if Z[1] == "x":
   Z.pop(1)
   Z.append(1)

if X[1] == "x":
   Z.pop(1)
   Z.append(1)

X = list(map(float, X))  # Converte todos os elementos da lista X para inteiros
Z = list(map(float, Z))  # Converte todos os elementos da lista Z para inteiros



#________________________________________________________________________________ teste


def inversa(X,Z):
   res0 = (X[0]*Z[0]) / X[1]
   print(f' | X = {res0}     I.P\n','|')

def direto(X,Z):
   res = (X[1]*Z[0])/X[0]
   print(f' | X = {res}     D.P\n\n\n\n\n')


inversa(X,Z)
direto(X,Z)


#_________________________________________________________________________________
#os.system('pause')



