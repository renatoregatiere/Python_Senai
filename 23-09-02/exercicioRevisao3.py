'''
-Faça um programa em Python que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido.
'''
n1 = int(input('Digite o número para mostrar a tabuada: '))
cont=0
while(cont<=10):    
    print(f'{n1} x {cont} = {n1*cont}')
    cont+=1
