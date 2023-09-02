'''
- Faça um algoritmo em linguagem Python que lê um número N digitado pelo usuário (esse número vai ser a quantidade de termos) imprime os N primeiros da sequência de Fibonacci.
'''

n1 = int(input('Digite a quantidade de termos: '))
cont=0
ultimo=1
penultimo=1
while(cont<=n1):
    termo=ultimo+penultimo
    penultimo = ultimo
    ultimo = termo
    cont+=1
    print(termo)