#Programa referente ao exercÌcio 4.
#númerosequencial, refere-se ao  número a ser encontrado na sequência de Fibonacci
#cont, é o contador para a função while
#numeroanterior, armazana o número anterior na sequência, o qual será somado
#numeroatual, refere-se ao número atual que será somado com o número anterior para obter o próximo número da sequência
#Previsto tratamento de erros
#Programadora: Barbara Bidoia Bidetti Turma B - Análise e Desenvolvimento de Sistemas
print("-"*60)
print("exercício 4, sequência de Fibonacci")
print("-"*60)
try:
    numerosequencial=int(input("Digite uma posição da sequência de Fibonacci (número inteiro e positivo) a qual deseje saber qual é o número correspondente: "))
    cont=1
    numeroanterior=0
    numeroatual=1
    while cont<numerosequencial:
        numeroanterior,numeroatual=numeroatual,numeroanterior+numeroatual
        cont+=1
    if numerosequencial<0:
        print(f'O número sequêncial é inválido, pois é negativo')
    else:
        print(f'O número correspondente à sequência é {numeroatual}')
except:
    print("O número sequêncial deve ser inteiro e positivo")