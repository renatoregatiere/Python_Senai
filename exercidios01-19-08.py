salario = int(input("digite o o seu salário: "));
if(salario <= 1800):
    reajustado = salario*1.15;
    reajuste = "15%";
elif(salario >= 1800 and salario <= 3700):
    reajustado = salario*1.11;
    reajuste = "11%";
else:
    reajustado = salario*1.075;
    reajuste = "7,50%";
print(f"O Salário era R$ {salario}, teve um reajuste de {reajuste} e foi para R$ {reajustado}")