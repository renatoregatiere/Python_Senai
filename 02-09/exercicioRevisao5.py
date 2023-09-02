'''
- Faça um programa que receba um número digitado e pelo usuário e calcule a soma de todos os números de 1 até o número digitado.
'''

n1 = int(input('Digite um número: '))
cont=1
soma=0
while(cont<=n1):
    soma=soma+cont
    cont+=1
print(f'A soma é {soma}')