'''
Um posto está vencendo combustíveis com a seguinte tabela de desconto:

Álcool:
até 20 litros: desconto de 3% por litro
acima de 20 litros: desconto de 5% por litro

Gasolina:
Até 20 litros; desconto de 4% por litro
Acima de 20 litros, desconto de 6% por litro

Crei um programa que leia o número de litros vendidos, o tipo de combustível(codificado da seguinte forma: A-álcool. G-gasolida), calcule e imprima o valor a ser pago pelo cliente.
O programa somente deve fazer o cálculo se o usuário digitar 'A' ou 'G'. Se digitar uma oção diferente o programa deve avisar e ser encerrado.
Considerar valores por liltro abaixo:
Gasolina: R$ 5,00
Álcool: R$ 2,90
'''
tipo = str(input("Escolha um tpo de combústivel:\nG - Gasolina\nA - Álcool\nDigite a opção: "))
gasolina=5
alcool=2.90

if(tipo!="a" and tipo!="A" and tipo!="g" and tipo!="G"):
    print("Tipo inválido")
else:
    litros = float(input("Digite a quantida de litros: "))
    if(tipo=='g' or tipo=='G' and litros<=20):
        vlr = (gasolina-gasolina*0.04)*litros
    elif(tipo=='g' or tipo=='G' and litros>20):
         vlr = (gasolina-gasolina*0.06)*litros
    elif(tipo=='a' or tipo=='A' and litros<=20):
        vlr = (alcool-alcool*0.03)*litros
    elif(tipo=='a' or tipo=='A' and litros>20):
        vlr = (alcool-alcool*0.05)*litros
    print(f"O preço a pagar é: {vlr}")