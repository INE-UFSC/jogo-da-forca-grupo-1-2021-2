def procura_letra(palavra, letras):
    for i in range(len(palavra)):
        if palavra[i] not in letras:
            palavra = palavra.replace(palavra[i], '_')
    if '_' not in palavra:
        status = 'venceu'
    elif letras[len(letras)-1] not in palavra:
        status = 'errou'
    else: 
        status = 'acertou'  
    return status, palavra
