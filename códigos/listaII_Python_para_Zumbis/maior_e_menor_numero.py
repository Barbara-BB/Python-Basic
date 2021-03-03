# Verificando qual é o maior e o menor número entre três números informados
numeroa=float(input("Digite o primeiro número:"))
numerob=float(input("Digite o segundo número:"))
numeroc=float(input("Digite o terceiro número"))

if numeroa==numerob==numeroc:
    print(f'Os três números são iguais a {numeroa}, então não há maior e menor número')
else:
    if numeroa>numerob and numeroa>numeroc:
        if numerob>numeroc:
            print(f'O maior número é {numeroa} e o menor número é {numeroc}')
        else:
            print(f'O maior número é {numeroa} e o menor número é {numerob}')
    else:
        if numerob>numeroc:
            if numeroa>numeroc:
                print(f'O maior número é {numerob} e o menor número é {numeroc}')
            else:
                print(f'O maior número é {numerob} e o menor número é {numeroa}')
        else:
            if numerob>numeroa:
                print(f'O maior número é {numeroc} e o menor número é {numeroa}')
            else:
                print(f'O maior número é {numeroc} e o menor número é {numerob}')
