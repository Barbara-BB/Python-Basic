n=int(input("Digite um número inteiro positivo a ser veriicadp se é primo: "))
# verifica se o número fornecido é primo
fator=2

if n%fator==0 and n!=2: # se o resto da divisão por 2 for zero e o número não for 2, não é primo
    print("não primo")
else:
    print("Primo") #caso contrário, é primo