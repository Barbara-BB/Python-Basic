ano=int(input("Digite o ano a ser verificado se é bissexto:"))
if ano%4==0 or ano%400==0 and ano%100!=0:
    print("O ano é bissexto")
else:
    print("O ano não é biseexto")