import math #importando a biblioteca para fazer cálculos matemáticos
a=int(input("Digite um número inteiro para a coordenada x do primeiro ponto: "))
b=int(input("Digite um número inteiro para a coordenada y do primeiro ponto:"))
c=int(input("Digite um número inteiro para a coordenada x do segundo ponto: "))
d=int(input("Digite um número inteiro para a coordenada y do segundo ponto: "))
# Acima coletando as coordenadas do primeiro e segundo ponto a ser calculado a distância
dist=math.sqrt(((c-a)**2)+((d-b)**2)) #fórmula para calcular a distância
if dist>=10: #Se for maior que 10 a distância imprime que é longe
    print("longe")
else: # Se não for imprime que é perto
        print("perto")