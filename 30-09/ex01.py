'''
Crie uma lista com 1.000 números com a ajuda do range(). 
O consjunto de número deve iniciar em -75. 
Ao final mostre esses números na tela e a quantidade de itens dentro da lista.
'''

lista = []
x = 1000 - 75
for i in range(-75,x):
    lista.append(i)  
print(f'Lista: {lista}\nQuantidade de números na lista: {len(lista)}')
