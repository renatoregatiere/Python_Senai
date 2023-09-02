'''
- Crei um programa que solicite a senha de uma usuária e depois peça para digitar novamente até que as duas senhas sejam correspondentes.
'''

n1 = int(input('Digite a senha: '))
n2 = int(input('Digite a senha novamente: '))

while(n1!=n2):
    print('Senha inválida, digite novamnete:')
    n1 = int(input('Digite a senha: '))
    n2 = int(input('Digite a senha novamente: '))
print(f'Senha válida!')