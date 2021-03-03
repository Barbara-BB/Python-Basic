#Programa referente ao exercÌcio 4.
#contpalavras é um contador.
#não considerei o texto como input, porque o testo já está definido no inicio do exercicio.
#Programadora: Barbara Bidoia Bidetti Turma B - Análise e Desenvolvimento de Sistemas
texto='''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''
texto=texto.lower()
texto=texto.replace('.','')
texto=texto.replace(',','')
texto=texto.replace(':','')
palavras=texto.split()
contpalavras=0
palavraidentificada=[]
while contpalavras!=len(palavras):
    palavraverificada=palavras[contpalavras]
    if palavraverificada[0]=="p" or palavraverificada[0]=="y" or palavraverificada[0]=="t" or palavraverificada[0]=="h" or palavraverificada[0]=="o" or palavraverificada[0]=="n":
        palavraidentificada.append(palavraverificada)
    if palavraverificada[len(palavraverificada)-1] == "p" or palavraverificada[len(palavraverificada)-1] == "y" or palavraverificada[len(palavraverificada)-1] == "t" or \
        palavraverificada[len(palavraverificada)-1] == "h" or palavraverificada[len(palavraverificada)-1] == "o" or palavraverificada[len(palavraverificada)-1] == "n":
        palavraidentificada.append(palavraverificada)
    contpalavras=contpalavras+1
print(f'O statement fornecido possui as seguintes palavras que começam ou terminam com uma das letras da palavra python {palavraidentificada}')
