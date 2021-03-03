a=int(input("Digite um número inteiro: "))
# Coleta o valor a ser verificado se é divisível por 3
x=a%3 # Verifica se o valor apresenta resto na divisão por 3
if x==0: # se não houver resto na divisão, é divisível por 3
    print("O número fornecido é divisível por 3")
else: # Caso contrário, não é divisível por 3
    print("Pena! Este número não é divisível por 3")