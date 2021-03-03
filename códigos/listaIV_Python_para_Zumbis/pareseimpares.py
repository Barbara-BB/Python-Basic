#Programa referente ao exercÌcio 2.
#cont é um contador.
#Programadora: Barbara Bidoia Bidetti Turma B - Análise e Desenvolvimento de Sistemas
import random
#sorteie 20 numeros de 1 a 100
numero=random.sample(range(1,100),20)
cont=0
par=[]
impar=[]
while cont<=19:
    if int(numero[cont])%2==0:
        par.append(numero[cont])
    else:
        impar.append(numero[cont])
    cont=cont+1

print(f'Os números pares dos vinte números sorteados entre 1 a 100 foram {par}')
print(f'Os números ímpares dos vinte números sorteados entre 1 a 100 foram {impar}')
