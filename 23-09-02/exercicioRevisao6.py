'''
- faça um programa que receba um valor inteiro, informe se o número é positivo ou netro.
'''

n1 = int(input('Digite um número: '))
if n1>0:
    print(f'O número {n1} é Positivo')
elif n1==0:
    print(f'O número {n1} é Neutro')
else:
    print(f'O número {n1} é negativo')