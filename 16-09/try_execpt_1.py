'''Faça um programa que pergunte o nome e o preço de três produtos e informe qual o produto você deve comprar, sabendo que a desisão é sempre pelo mais barato. O programa deve validar a entrada de dados atavés do try-exept e o preço dos produtos deve ser sempre positivo.'''

i=1
anterior = 1000000
qtdProduto = 3

print(f'\nDigite {qtdProduto} nomes de produtos e seus preços!')

while (i<=qtdProduto):       
    try:  
        nomeProduto = str(input(f'\nDigite o nome do {i}º produto: '))   
        valorProduto = int(input(f'Digite o valor do {nomeProduto}: '))
        if (valorProduto < anterior):
            maisbarato = str.upper(f'\nVocê deve comprar o produto {nomeProduto} pois ele é o mais barato!\n')
            anterior=valorProduto
    except:
        print(f'O número digitado não é do tipo inreteiro')
        i=i-1      
    i=i+1    
print(maisbarato)