'''
leia duas strings, verifique se a segunda ocrre dentro da primeira e imprima a posição de ínicio
'''

primeira = input('Digite um texto: ')
segunda = input('Digite outro texto: ')

posicao = primeira.find(segunda)

print(posicao)