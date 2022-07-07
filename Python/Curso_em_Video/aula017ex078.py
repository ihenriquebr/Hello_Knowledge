# Módulos
import emoji
# Cores
bbe = '\033[44m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f'{bbe} Maior {cc} :arrow_up:   {bbe} Menor {cc} :arrow_down:   {bbe} Posição {cc} :on:',use_aliases=True))
# Estruturas
nums = []
pos = 0
for rep in range(0, 5):
    nums.append(int(input(f'Valor da posição {rep}: ')))
print(nums)
maior = 0
pm = 0
for p, n in enumerate(nums):
    print(p, n)
    # Maior
    if n > maior:
        maior = n
        pm = p
    else:
        maior = maior
        pm = pm
print(f'Posição: {pm} Maior: {maior}')
# todo terminar menor