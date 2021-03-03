n=int(input("Digite o número a ser fatorado: "))
# número a ser fatorado
f=1 # se o número for menor que zero, a faotração é igual a 1
while n>0:
    f=f*n #multiplicando os fatores
    n=n-1 # calculando pela fórmula o próximo número da fatoração
print(f)# imprimindo o resultado
