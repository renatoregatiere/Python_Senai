'''
Crie um programa que recebe dois números e pergunte ao usuário o que ele deseja fazer.
1 - exponenciação / 2 - Raiz quadrada dos dois números. / 3 - verificar se o 1º número é multilo do 2º.
Regra: somente ´numeros entre 0 e 1000 devem ser aceitos. Os cálculos deverão ser feitos em funções separadas do arquivo principal.
Função em python para calcular raiz quadrada: math.sqrt() (deve-se importar a classe 'math')
'''
import math

op = int(input('O que deseja?\n1 - exponenciação\n2 - Raiz quadrada dos dois números.\n3 - verificar se o 1º número é multiplo do 2º\nOpção: '))

while(op!=1 and op!=2 and op!=3):
   op = int(input('Opção inválida, digite novamente\nO que deseja?\n1 - exponenciação\n2 - Raiz quadrada dos dois números.\n3 - verificar se o 1º número é multiplo do 2º\nOpção: ')  ) 

if(op==2):
    print('\n## Opção Raiz quadrada ##')
    num = int(input('Digite um número para calcualr a raiz quadrada: '))
    result = math.sqrt(num)
elif(op==1):
    print('\n## Opção Expoenciação ##')
    num = int(input('Digite um número: '))
    num2 = int(input('Digite o número que será elevado: '))
    result = num**num2
elif(op==3):
    print('\n## Opção Verificar se número é Multiplo ##')
    num = int(input('Digite um número: '))
    num2 = int(input('Digite mais um número: '))
    if(num%2==0):
        result = f'O número {num} é multiplo de {num2}'
print(f'Resultado: {result}')