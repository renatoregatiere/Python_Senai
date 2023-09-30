'''
Crei um programa que receba um nome completo de uma pessoa.
Crei duas listas: uma lista para armazenar as vogais 'e' 'o'u't'r'a' para armazenar as consoantes do nome.
Ao final, exiba as duas listas na tela utilizando o comando for.
'''
nome= input('Digite seu nome: ')
listaV = []
listaC = []
vogais = ['a','e','i','o','u']
for i in nome:
    if i in vogais:
        listaV.append(i)
    else:
        listaC.append(i)
print(f'Vogais: {listaV}\nConsoantes: {listaC}')