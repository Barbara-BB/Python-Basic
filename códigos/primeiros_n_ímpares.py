# verifica sequencialmente quantos números impares existem, por exemplo os cinco primeiros números ímpares
n=int(input("Digite uma quantidade numeros impares desejados: "))
i=0 # inicializando somador
while n>=1: # enquanto a quantidade de números for maior ou igual a 1
    i=i+1 #soma 1 para verificar se é impar
    if i%2!=0: # se não for divisível por 2, é ímpar
        print(i) # imprime o número
        n=n-1 # tira um da contagem de números ímpares a serem apresentadas