# Módulos
import emoji
# Cores
gn = '\033[42m'
cc = '\033[m'
# Abertura
print(emoji.emojize(f':soccer: {gn} Brasileirão 2022 {cc} :soccer:',use_aliases=True))
# Lista dos 20 primeiros colocados
times = ('Corinthians', 'Palmeiras', 'São Paulo', 'Atlético Mineiro', 'Botafogo', 'Santos', 'Fluminense', 'Coritiba', 'América-MG', 'Avaí', 'Internacional', 'Athletico-PR', 'Bragantino', 'Flamengo', 'Goiás', 'Atlético-GO', 'Juventude', 'Ceará', 'Fortaleza')
# 5 primeiros
print(times[0:5])
# 4 últimos