#Calculando se há excedente e multa na pesca
peso=float(input("Digite o peso total de peixes pescados:"))
if peso>50:
    excesso=peso-50
    multa=excesso*4

    print("O peso excedente é:",excesso,"Kg")
    print("A multa a ser paga R$:",multa)
else:
    print("O peso excedente é 0")
    print("A multa é 0")
