
#Programa referente ao exercÌcio 2.
#nome, recebe valor do usuário
#senha, recebe valor do usuário
#Programadora: Barbara Bidoia Bidetti Turma B - Análise e Desenvolvimento de Sistemas
print("-"*40)
print("exercício 2, comparando senha e nome")
print("-"*40)
nome=input("Escreva seu nome: ")
senha=input("Cadastre sua senha: ")
while nome==senha:
    print("A sua senha não pode ser igual ao seu nome, digite uma nova senha")
    senha = input("Digite uma senha válida: ")
print("Seu nome e senha foram registrados")