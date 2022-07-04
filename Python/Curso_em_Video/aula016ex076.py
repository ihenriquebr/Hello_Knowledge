# Módulos
import emoji
# Cores
byw = '\033[1;43m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':radio: {byw} Produtos e Preços {cc} :credit_card:',use_aliases=True))
# Lista
lista = ('Lápis', 2.00,
         'Borracha', 1.50,
         'Caderno', 20.00,
         'Caneta', 1.75,
         'Mochila', 30.00)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]}')
    else:
        print(f'{lista[pos]}')
#todo terminar frases do FOR