'''
Crei uma lista de 50.000 números (range()) e imprima na tela esta lista, mas somente os números ímpare.
'''

lista = []
for i in range(0,5000):
    if(i%2==1):
        lista.append(i)    
print(lista)