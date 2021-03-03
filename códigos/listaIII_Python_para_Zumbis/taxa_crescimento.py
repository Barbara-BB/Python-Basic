#Programa referente ao exercÌcio 3.
#Programadora: Barbara Bidoia Bidetti Turma B - Análise e Desenvolvimento de Sistemas
print("-"*60)
print("exercício 3, igualar populações")
print("-"*60)
cont=0
A=80000
B=200000
while A <= B:
    A=A+0.03*A
    B=B+0.015*B
    cont=cont+1
print(f'A população de A irá ultrapassar a população de B em {cont} anos')