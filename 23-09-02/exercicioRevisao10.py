'''
- Ao receber o salário atual de um funcionário, calcule o valor do novo salário, ajustado de acordo com a tabela abaixo:
abaixo de R$ 500,00 reajuste 15%
de R$ 500,00 até R$ 1.000,00 reajuste 10%
acima R$ 1.000,00 reajuste 5%
'''

salario = float(input('Digite o salário: '))
if(salario<500):
    salarioreajustado = salario*1.15
    perc = '15%'
elif(salario>= 500 and salario<=1000):
    salarioreajustado = salario*1.10
    perc = '10%'
else:
    salarioreajustado=salario*1.05
    perc = '5%'
print(f'O salário R$ {salario:5.2f} teve um reajuste de {perc} e foi para R$ {salarioreajustado:5.2f}')

