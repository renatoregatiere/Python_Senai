#7 - atribua o nome de uma cidade a uma variável. Se o nome da cidade tiver menos de 10 caracteres, o sistema deve informar: 'O nome da cidade de 'cidade' tem menos de 10 caracteres. Senão deve informar: 'o nome da cidade de 'cidade' tem x caracteres'.
print("exercidio 7:")
cidade = "São Jose do Rio Preto"
if(len(cidade)<10):
    print(f"{cidade} tem menos de 10 caracteres.")
else:
    print(f"{cidade} tem {len(cidade)} caracteres")

#8 - Atribua dois nomes de pessoas a duas variáveis e verifique quais dos dois nomes tem a maior quantidade de caracteres. No final o sistema deve mostrar: 'O nome 'nome' é maior que o nome 'nome2'.
print("\nexercidio 8:")
nome1 = "Renato"
nome2 = "Rodrigo"
if(len(nome1)>len(nome2)):
    print(f"O nome {nome1} é maior que o nome {nome2}")
else:
    print(f"O nome {nome2} é maior que o nome {nome1}")

#9 - Atribua o nome de um estado brasileiro a uma variável. O fonte deve pegar do 3 ao 7 caractere do nome e mostra-lo na tela. O fonte deve verificar se o nome do estado digitado possui pelo menos 7 caracteres. Se possuir menos de 7 caracteres o programa deve ser encerrado.
print("\nexercidio 9:")
estado = "São Paulo"
if(len(estado)>7):
    print(estado[3:7])
else:
    print(f"o {estado} possuí menos de 7 caracteres")

#10 - Atribua seu nome completo a uma variável. Crie para cada nome (sobrenome) uma variável separada (através do fatiametno de strings) e depois mostre cada nome e sobrenome em linhas diferentes.
print("\nexercidio 10:")
nomeCompleto = "Renato Regatiere"
teste = nomeCompleto.split()
primeirNOme = nomeCompleto[:6]
sobrenome = nomeCompleto[7:]
print(f"nome: {primeirNOme}\nSobrenome: {sobrenome}")
