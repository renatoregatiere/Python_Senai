#1 - Atribua seu nome completo a uma variável e mostre na tela o 13º caractere do seu nome
print("Atividade 1:")
nome = "Renato Regatiere"
print(len(nome))
print(nome[12])

#2 - atribua seu nome completo a uma varivael, crei outra variavel onde você irá armazenar o 3º caractere do seu nome "somado" com 15º. Mostre essa "soma" na tela.
print("\nAtividade 2:")
nome2 = "Renato Regatiere"
nome13 = nome[12:13]
nome15 = nome[14:15]
print(nome13+nome15)
print("Atividade 1:")
#3 - Atribua seu 1º nome a uma variável, multiplique por 50 os três primeiros caracteres do seu nome e mostre a mensagem na tela com o resultado.
print("\nAtividade 3:")
nome3 = "Renato Regatiere"
msg = nome[0:3]*50
print(msg)

#4 - Crei um programa que atribua a uma variável um nome qualquer. Se o nome tiver mais de 6 caracteres, moestre na tela a seguinte informação: '(nome)ABCDEF' Senão mostre na tela: '(nome) tem menos de 7 caractere'.
print("\nAtividade 4:")
nome4 = "Renato Regatiere"
if(len(nome4)>=6):
    print(f"{nome} ABCDEF")
else:
    print(f"{nome4} tem menos de 6 caractere")

#5 - Mostre na tela a seguinte mensagem usando compsições %s, %d e %f: 'Juliano tem 1.72 de altura e pesa 00080 kilos.' O nome, a altura e o peso devem ser atribuídos em variávis.
print("\nAtividade 5:")
nome5 = "Juliano"
altura = 1.72
peso = 80
print("%s tem %.2f de altura e pesa %05d kilos"%(nome,altura,peso))

#6 - Mostre a mesma mensagem anterior mas utilizando o '.format()' e o 'f-string' (mostrar duas mensagens, uma para cada metodologia)
print("\nAtividade 6:")
print("{} tem {} de altura e pesa {:05d} kilos".format(nome5,altura,peso))
print(f"{nome5} tem {altura} de altura e pesa {peso:05d}")