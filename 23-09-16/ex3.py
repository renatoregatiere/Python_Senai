'''
Faça um programa que receba quantos números o usuário deseja digitar.
O Programa deve fazer a somatória de todos os números digitados e depois mostrar esse somatória na tela
'''
i=1
soma=0
qtdNumeros = int(input('Quantos números você vai digitar?: '))
while(i<=qtdNumeros):
    n = int(input(f'Digite o {i}º número: '))
    soma=soma+n    
    i=i+1
print (f'\nA soma dos valores é igual à {soma}')