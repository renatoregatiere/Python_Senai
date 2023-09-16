'''
Crie um programa que receba um valor inteiro e calcule a sua tabuada, iniciando do 10 até o 0. O programa deverá também contar quantos números multiplos de 3 serão gerados na tabuada. O usuário deverá digitar apenas valores entre -500 e 500. Válidar entrada de dados com try-execept.
'''
i = 10
multiplos3=0
try:
    tabuada = int(input('Qual tabuada você quer?: '))
    if(tabuada>=-500 and tabuada<=500):
        while True:          
                if i>=0:           
                    print(f'{tabuada} * {i} = {tabuada*i}')         
                    if(tabuada*i)%3==1:
                        multiplos3 = multiplos3+1   
                    i=i-1
                else:
                    break
        print(f'Multiplos: {multiplos3}')
    else:
        print('erro!\nDigite um número entr -500 e 500')
        
except:
    print('Apenas Números são permitidos')

       
