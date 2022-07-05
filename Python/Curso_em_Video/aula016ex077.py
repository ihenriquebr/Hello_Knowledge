# Módulos
import emoji
# Cores
bgy = '\033[1;47m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':capital_abcd: {bgy} Palavras e Vogais {cc} :a:',use_aliases=True))
# Tupla
palavras = ('APRENDER', 'PROGRAMAR', 'MNB')
# Estruturas

for a in palavras:
    print(f'A palavra {a} tem as vogais: ',end='')
    cont = 0
    for b in a:
        if b == "A":
            cont += 1
            print("a",end=' ')
        if b == "E":
            cont += 1
            print("e",end=' ')
        if b == "I":
            cont += 1
            print("i",end=' ')
        if b == "O":
            cont += 1
            print("o",end=' ')
        if b == "U":
            cont += 1
            print("u",end=' ')
        else:
            continue
    if cont == 0:
        print('não há vogais nesta palavra.')
    cont = 0
    print('')
# todo terminar as palavras
