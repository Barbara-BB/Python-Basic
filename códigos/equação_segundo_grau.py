import math
a=float(input("Digite o coeficiente A da equação do 2 grau: "))
b=float(input("Digite o coeficiente B da equacão do segundo grau: "))
c=float(input("Digite o coeficiente C da equação do segundo grau: "))
# Coletando os coeficientes da equação do segundo grau
delta=(b**2)-(4*a*c) # Calculando o delta
if delta>0: # Se o delta é maior que zero, temos duas raízes
    rt = math.sqrt(delta) # extraindo a raiz quadrada de delta
    raiz1 = (-b + rt) / (2 * a) # calculando a primeira raiz
    raiz2 = (-b - rt) / (2 * a) # calculando a segunda raiz
    if raiz1<raiz2: # imprime a raiz na ordem
        print("as raízes da equação são",raiz1,"e",raiz2)
    else:
        print("as raízes da equação são", raiz2, "e", raiz1)
else:
       if delta==0: # Se o delta é igual a zero, temos uma raiz
        raiz3 = (-b / (2 * a))
        # Imprimindo uma única raiz
        print("a raiz desta equação é ",raiz3)
       else: # Se o delta é negativo, não existe solução nos conjuntos dos reais
        print("esta equação não possui raízes reais")

