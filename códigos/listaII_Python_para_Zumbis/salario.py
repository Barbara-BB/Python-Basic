ganhohora=float(input("Qual é o valor do salário recebido por hora: "))
horatrabalhada=float(input("Digite as horas trabalhadas no mês: "))
salariobruto=ganhohora*horatrabalhada
ir=salariobruto*0.11
inss=salariobruto*0.08
sindicato=salariobruto*0.05
salarioliquido=salariobruto-ir-inss-sindicato
salariobruto=round(salariobruto,2)
ir=round(ir,2)
inss=round(inss,2)
sindicato=round(sindicato,2)
salarioliquido=round(salarioliquido,2)

print(f'O salário bruto é de R${salariobruto}, sendo descontado R${ir} para o imposto de renda, R${inss} para o inss e R${sindicato} para o sindicato. Sendo assim o salário líquido é de R${salarioliquido}')