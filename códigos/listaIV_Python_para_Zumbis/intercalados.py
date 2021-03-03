#Programa referente ao exercÌcio 3.
#cont é um contador.
#Programadora: Barbara Bidoia Bidetti Turma B - Análise e Desenvolvimento de Sistemas
#sorteie 10 numeros de 1 a 100
lista1=random.sample(range(1,100),10)
lista2=random.sample(range(1,100),10)
lista3=[]
cont=0
while cont<=9:
    lista3.append(lista1[cont])
    lista3.append(lista2[cont])
    cont=cont+1
print(f'Os dez números sorteados entre 1 a 100 foi o número {lista1} na primeira lista')
print(f'Os dez números sorteados entre 1 a 100 foi o número {lista2} na segunda lista')
print(f'Intercalando os números da primeira lista com a segunda lista, obteve-se a terceira lista {lista3}')
