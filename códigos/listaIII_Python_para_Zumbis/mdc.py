#Programa referente ao exercÌcio 5.
#A, pede o primeiro número para o MDC
#B, pede o segundo número para o MDC
#A função if é para inverter o número se o primeiro digitaodo for menor que o segundo
#Programadora: Barbara Bidoia Bidetti Turma B - Análise e Desenvolvimento de Sistemas
print("-"*60)
print("exercício 5, MDC")
print("-"*60)
A=int(input("Digite o primeiro número: "))
B=int(input("Digite o segundo número: "))
if A<B:
    A,B=B,A
while B!=0:
    A,B=B,A%B

print(f'O MDC é: {A}')