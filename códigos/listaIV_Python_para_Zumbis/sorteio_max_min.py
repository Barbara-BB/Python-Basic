#Programa referente ao exercÌcio 1.
#contmaior e contmenor são contadores
#posicaomaior e posicaomenor são referencias da posicão dos números na lista
#numeromaior e numeromenor são os numeros identificados como maior e menor na lista numero, incialmente começam com o primeiro numero da lista pois a condição if não o contempla se for verdadeira
#Programadora: Barbara Bidoia Bidetti Turma B - Análise e Desenvolvimento de Sistemas
import random
#sorteie 10 numeros de 1 a 100
numero=random.sample(range(1,100),10)
contmaior=1
contmenor=1
numeromaior=int(numero[0])
numeromenor=int(numero[0])
posicaomaior=0
posicaomenor=0
print(numero)
while contmaior<=9:
    if numeromaior<int(numero[contmaior]):
        numeromaior=int(numero[contmaior])
        posicaomaior=contmaior
        contmaior=contmaior+1
    else:
        contmaior=contmaior+1
while contmenor <= 9:
    if int(numero[contmenor]) < numeromenor:
        numeromenor = int(numero[contmenor])
        posicaomenor = contmenor
        contmenor=contmenor+1
    else:
        contmenor=contmenor+1


print(f'O maior número dos dez números sorteados entre 1 a 100 foi o número {numeromaior} e a posição deste número na lista dos dez números sorteados foi {posicaomaior}, considerando que a posição inicial é zero')
print(f'O menor número dos dez números sorteados entre 1 a 100 foi o número {numeromenor} e a posição deste número na lista dos dez números sorteados foi {posicaomenor}, considerando que a posição inicial é zero')
