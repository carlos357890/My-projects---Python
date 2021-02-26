def jogar():
    print("_"*30)
    print("*"*20+"JOGO DA FORCA"+"*"5)
    print("_"*30)

    palavra_secreta = "banana"
    letras_acertadas = ['_', '_', '_', '_', '_', '_']

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):
        chute = str(input("Qual a letra? "))