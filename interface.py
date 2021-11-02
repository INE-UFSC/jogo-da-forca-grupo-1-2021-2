import os

boneco = (('   ','   ','   ',''
),(
    ' O ','   ','   ',''
),(
    ' O ',
    ' | ','   ',''
),(
    ' O ',
    '/| ','   ',''
),(
    ' O ',
    '/|\\','   ',''
),(
    ' O ',
    '/|\\',
    '/  ',''
),(
    ' O ',
    '/|\\',
    '/ \\',''
),(
    ' X ',
    '/|\\ ',
    '/ \\',''
))
forca = (
    '|  ',
    '|  ',
    '|  ',
    '|  ',
    '_____')

#exemplo de uso: interfaceJogo(0, ['a','b','c'], '___a') ou interfaceJogo(3, 'abc', ['_','_','_','a'])
#o jogador vai ter 7 tentativas
#vitoria_derrota - 0=derrota, 1=normal, 2=vitoria
largura = 45
def interfaceJogo(erros, letras_inseridas, palavra_display, vitoria_derrota=1):
    os.system('cls||clear')
    print('-'*45)
    if vitoria_derrota == 0:
        print('\033[1;31;40mDERROTA'.center(largura+9))
    elif vitoria_derrota == 1:
        print(f'Tentativas restantes: {7 - erros}')
    elif vitoria_derrota == 2:
        print('\033[1;32;40mVITORIA'.center(largura+9))

    print('\033[0;37;40m'+forca[-1])
    letras_inseridas = ', '.join(letras_inseridas)
    palavra_display = ' '.join(palavra_display)
    for i in range(4):
        print(forca[i]+boneco[erros][i], end='')
        if i == 0:
            print(' '*10,letras_inseridas,end='')
        elif i == 2:
            print(' '*5,f'{palavra_display}'.center(largura - 12),end='')
        print()
    print('-'*45)

interfaceJogo(0, ['a','b','c'], '___a',2)