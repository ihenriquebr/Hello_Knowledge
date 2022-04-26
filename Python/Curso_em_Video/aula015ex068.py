# Módulos
import emoji
import random
# Cores
byw = '\033[30;43m'
yw = '\033[1;33m'
co = '\033[1;36m'
gn = '\033[32m'
rd = '\033[31m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':fist: {byw} Jogo do Par ou Ímpar {cc} :v:',use_aliases=True))
# Estruturas
soma = 0
cont = 0
while True:
    maokalista = random.randint(0,1)
    par = int(input(emoji.emojize(f'Digite [{yw}2{cc}] para escolher {yw}PAR{cc} OU [{yw}3{cc}] para escolher {yw}ÍMPAR{cc}\n',use_aliases=True)))
    if par == 2 or par == 3:
        mao = int(input(emoji.emojize(f'Digite [{co}0{cc}] para escolher {co}ZERO{cc} :fist: OU [{co}1{cc}] para escolher {co}UM{cc} :point_up:\n',use_aliases=True)))
        if mao == 0 or mao == 1:
            print(mao, maokalista)
            if par == 2:
                if mao == 0 and maokalista == 0:
                    cont += 1
                elif mao == 1 and maokalista == 1:
                    cont += 1
                else:
                    break
            elif par == 3:
                if mao == 0 and maokalista == 1:
                    cont += 1
                elif mao == 1 and maokalista == 0:
                    cont += 1
                else:
                    break
        else:
            print(f'{rd}Erro!{cc} Por favor, digite {gn}ZERO{cc} ou {gn}UM{cc}!')
    else:
        print(f'{rd}Erro!{cc} Por favor, digite {gn}ZERO{cc} ou {gn}UM{cc}!')
    