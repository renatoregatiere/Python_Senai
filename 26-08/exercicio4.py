'''
Faça um programa que faça 5 perguntas para uma pessoal sobre um crime, as perguntas são:
    Telefoneou para a vítima?
    Esteve no local do crime?
    Mora perto da vítima?
    Devia para a vítma?
    Já trabalhou com a vítima?
O programa de deve no final emitir uma classificação sobre a participação da pessoal no crime.
Se a pessoal responder positivamente a 2 questão, ela deve ser classificada como 'Suspeita', entre 3 e 4 como 'Cumplice' e 5 como 'Assassino'.
Caso qtdrário, ele será classificado como 'inocente'.
'''

qtd=0
print("\nDigite um SIM ou NÃO para as perguntas abaixo:z\n")

resposta = []
classificacao=["Inocente","Suspeito","Cumplice","Cumplice","Assassino","Assassino"]
resposta.append(str.upper(input("Telefonou para a vitima?\n")))
resposta.append(str.upper(input("Esteve no local do crime?\n")))
resposta.append(str.upper(input("Mora perto da vitima?\n")))
resposta.append(str.upper(input("Devia para a vitima?\n")))
resposta.append(str.upper(input("Já trabalhou com a vitima?\n")))

for n in resposta:
    if(n=="SIM"):
        qtd+=1       
print(classificacao[qtd])