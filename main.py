# Código de um jogo da forca
from procura_letra import procura_letra
from banco import palavra
from interface import interfaceJogo

print("-"*20)
print("Jogo da Forca")
print("-"*20)

letras_digitadas = []
tentativas = 7
palavra = palavra()
erros = 0

while True:
    letra = input("Digite uma letra: ").lower()
    while (letra not in "abcdefghijlmnopqrstuvxz") or (len(letra) > 1) or (letra in letras_digitadas):
        letra = input("Digite uma letra: ").lower()
    letras_digitadas.append(letra)
    procura_letra(palavra, letras_digitadas)
    if status == "errou":
        erros += 1
    interfaceJogo(erros, letras_digitadas, palavra_display)

    if erros == tentativas:
        interfaceJogo(erros, letras_digitadas, palavra_display)
        break


