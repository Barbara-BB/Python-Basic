a=int(input("Digite um número inteiro: "))

# Coleta o valor a ser verificado se é divisível por 3 e 5
x=a%5 # Verifica se o valor apresenta resto na divisão por 5
y=a%3 # Verifica se o valor apresenta resto na divisão por 3
if x==0 and y==0: # Se não houver resto nas duas divisões acima, é divisível por 3 e por 5
    print("O número fornecido é divisível por 3 e 5")
else: # Caso contrário, não é.
    print("Pena! Este número não é divisível por 3 e 5")