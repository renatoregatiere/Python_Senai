n1 = int(input("Digite um valor: "))
if(n1 <= 0):
    print("Número inválido!")
else:
    if(n1 > 0 and n1 < 1000):
        result = n1*10
        cont = "Multiplicado"        
    elif(n1 >= 1000):
        result = n1 / 10
        cont = "Dividido"        
    print(f"{n1} {cont} por 10 é: {result}")