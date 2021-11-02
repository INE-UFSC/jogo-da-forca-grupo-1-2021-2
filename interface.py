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

largura = 45
def interfaceJogo(erros, letras_inseridas, palavra_display):
    os.system('cls||clear')
    print('-'*45)
    print(f'Tentativas restantes: {7 - erros}')
    print(forca[-1])
    letras_inseridas = ', '.join(letras_inseridas)
    palavra_display = ' '.join(palavra_display)
    for i in range(4):
        print(forca[i]+boneco[erros][i], end='')
        if i == 0:
            print(' '*5,f'{letras_inseridas}'.center(largura - 12),end='')
        elif i == 2:
            print(' '*5,f'{palavra_display}'.center(largura - 12),end='')
        print()
    print('-'*45)

interfaceJogo(0, ['a','b','c','d'], '___a')