seg=input("Por favor, entre com o número de segundos que deseja converter: ") # Coletando os segundos a serem convertidos
seg1=int(seg)#transformando o valor coletado em inteiro
dia=seg1//86400 #identificando quantos dias inteiros tem no valor fornecido
dia1=seg1%86400 #identificando o resto dos segundos fornecidos que não equivalem a um dia
horas=dia1//3600 #identificando da parte que não são dias quantos equivalem a horas
seg1rest=dia1%3600 #identificando o resto que não equivalem a hora
min=seg1rest//60 #identificando do resto que não equivale a hora, quantos são minutos
seg1rest1=seg1rest%60 #o resto que não equivale aos minutos são segundos
print(dia,"dias,",horas,"horas,",min,"minutos e",seg1rest1,"segundos.") #imprimindo o dia,hora, minuto e segundos
