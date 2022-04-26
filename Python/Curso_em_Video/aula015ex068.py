# Módulos
import emoji
# Cores
byw = '\033[30;43m'
yw = '\033[1;33m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':fist: {byw} Jogo do Par ou Ímpar {cc} :v:',use_aliases=True))
# Estruturas
mao = int(input(emoji.emojize(f'Digite [{yw}0{cc}] para escolher {yw}PAR{cc} :fist: OU [{yw}1{cc}] para escolher {yw}ÍMPAR{cc} :point_up:',use_aliases=True)))
