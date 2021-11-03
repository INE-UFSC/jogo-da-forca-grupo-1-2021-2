# Código de um jogo da forca
from procura_letra import *
from banco import *
from interface import *

print("-"*20)
print("Jogo da Forca")
print("-"*20)

letras_digitadas = []
tentativas = 7
palavra_secreta = palavra()
erros = 0

while True:
    letra = input("Digite uma letra: ").lower()
    while (letra not in "abcdefghijlmnopqrstuvxz") or (len(letra) > 1) or (letra in letras_digitadas):
        letra = input("Digite outra letra: ").lower()
    letras_digitadas.append(letra)
    status, palavra = procura_letra(palavra_secreta, letras_digitadas)
    if status == "errou":
        print("Você errou")
        erros += 1
    interfaceJogo(erros, letras_digitadas, palavra, 1)

    if erros == tentativas:
        print("Derrota")
        interfaceJogo(erros, letras_digitadas, palavra, 0)
        break

    if palavra == palavra_secreta:
        print("Parabéns! Você acertou a palavra secreta")
        interfaceJogo(erros, letras_digitadas, palavra, 2)
        break
