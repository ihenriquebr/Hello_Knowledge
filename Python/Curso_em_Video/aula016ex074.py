# Módulos
import emoji
import random
# Cores
bbe = '\033[44m'
we = '\033[1m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':repeat: {bbe} Números aleatórios {cc} :repeat:',use_aliases=True))
# Números
numeros = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))
print(numeros)