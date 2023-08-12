'''1 – Crie um algoritmo e um fluxograma que receba um número. Se o número for maior que
1000 o programa deve dividi-lo por 50. Se o número for menor ou igual a 1000 o programa deve
elevá-lo à potência 2.'''
n1 = int(input("digtie um numero: "))
if n1>=1000:
 print (n1/50)
else: print (n1**2)

'''2 – Crie um algoritmo que receba a idade de uma pessoa.
Se a idade for maior que 0 e menor que 12 o algoritmo deve imprimir na tela: Criança
Se a idade for maior ou igual a 12 e menor que 18 deve imprimir: Adolescente
Se a idade for maior ou igual a 18 deve imprimir: Adulto'''
idade = int(input("digite sua idade: "))
if idade>0 and idade<12:
    print ("Criança)")
elif idade>=12 and idade<=18:
    print ("Adolescente")
else: print("adulto")


'''3 – Crie um algoritmo e um fluxograma que receba um valor.
Se o valor for par, imprima na tela: Este número é par.
Se o valor for ímpar, imprima na tela: Este número é ímpar.'''
n1 = int(input("Digite um número: "))
if n1%2==0:
    print("Este número é par")
else: print("Este número é impar")