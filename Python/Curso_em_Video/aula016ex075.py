# Módulos
import emoji
# Cores
bgn = '\033[42m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':four_leaf_clover: {bgn} Quatro Valores {cc} :four_leaf_clover:',use_aliases=True))
# Números
ordem = 'Primeiro'
numeros = ()
for a in range(0,4):
    num = int(input(f'{f"Primeiro número: " if a == 0 else "Outro número: "}'))
print(numeros)