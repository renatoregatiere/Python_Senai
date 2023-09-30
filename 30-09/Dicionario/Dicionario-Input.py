paises = {
    'Brasil':'Sul-americano',
    'Chele':'Sul-americano',
    'EUA':'norte-americano'
}
while(True):
    pais = input('Digite o nome do país: ')
    if (pais == 'fim'):
        break
    continente = input(f'Digite o nome do continente do {pais}: ')
    paises.update({pais:continente})
for c,v in paises.items():
    print(f'Pais: {c} | contiente: {v}')