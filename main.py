# Código de um jogo da forca
# Fazer os imports

from banco import palavra

letras_digitadas = []
tentativas = y
# Estabelecer o número de tentativas (Boneco)
palavra = palavra()
# Recebe uma palavra aleatória do banco
erros = 0

# Chama a interface

while True:
    letra = input("Digite uma letra: ").lower()
    while (letra not in "abcdefghijlmnopqrstuvxz") or (len(letra) > 1) or (letra in letras_digitadas):
        letra = input("Digite uma letra: ").lower()
    letras_digitadas.append(letra)

# Chama as funções
    ...
    
    if erros == tentativas:
        break


