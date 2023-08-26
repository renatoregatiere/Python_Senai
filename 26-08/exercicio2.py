'''crie um programa que controle reservas de hotel e mostre um menu com 3 opções ao usuário
1 - fazer reserva
2 - encerrar reserva
3 - sair do programa

caso o usuário escolha a opção 1, o sistema deve receber o nome do cliente e quantos dias ele ficará hospedado.
Mostre uma previsão de valortotal a pagar sabendo que a diária do hotel é de R$ 80,00,.
Caso opção 2, o sitema deve receber o CPF e a quantidade de dias que o cliente ficou hospedado e mostre o total do valor a pagar.
Caso opção 3, o sitema deve ser encerrado. MOstre uma mensagem na tela.
'''
opcao=int(input("Olha uma das opções abaixo:\n1 - fazer reserva\n2 - encerrar reserva\n3 - sair do programa\nOpção: "))
if(opcao==1):
    nome=str(input("Digite seu nome: "))
    dias=int(input("Digite a quantidade de dias que ficará hospedado: "))
    soma=dias
    print(f"A previsão a pagar é de: {soma*80:5.2f}")
elif(opcao==2):
    cpf=str(input("Digite seu CPF: "))
    dias=int(input("Digite a quantidade de dias que ficará hospedado: "))
    soma=dias
    print(f"A previsão a pagar é de: {soma*80:5.2f}")
elif(opcao==3):
    print("Programa encerrado!")
else:
    print("Opção inválida")