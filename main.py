# Código de um jogo da forca
# Fazer os imports

letras_digitadas = []
tentativas = y
# Estabelecer o número de tentativas (De acordo com o tamanho da palavra?)
palavra = x 
#recebe uma palavra aleatória do banco
erros = 0

for i in range(tentativas):
    letra = input("Digite uma letra: ").lower()
    while (letra not in "abcdefghijlmnopqrstuvwz") or (len(letra) > 1) or (letra in letras_digitadas):
        letra = input("Digite uma letra: ").lower()
    letras_digitadas.append(letra)


    
    if erros == tentativas:
        break
