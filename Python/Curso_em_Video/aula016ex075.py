# Módulos
import emoji
# Cores
bgn = '\033[42m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':four_leaf_clover: {bgn} Quatro Valores {cc} :four_leaf_clover:',use_aliases=True))
# Números
num = tuple(int(input(f'{"Primeiro" if c == 1 else "Outro"} valor: '))for c in range(1,5))
# Vezes do 9
nove = num.count(9)
print(f'O número 9 {"não apareceu" if nove == 0 else "apareceu"} {f"{nove} vezes" if nove > 0 else "nenhuma vez"}.')
# todo 60% concluído.