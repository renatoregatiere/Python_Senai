'''crie um programa que recebe 3 valores inteiros e verifiqeu se são números positivos. Se pelo menos um número for negativo o sistema deve informar: 'somente números positivos são aceitos'. Se forem todos positivos, o programa deve encontrar qual deles é o maior e mostrá-lo na tela. Verificar se todods valroes são iguais. Dica para pegar o maior valor: função 'max()'''


n1 = int(input("digite um valor: "))
n2 = int(input("digite outro valor: "))
n3 = int(input("digite mais um valor: "))

if(n1<0 or n2<0 or n3<0):
    print("somente números positivos são aceitos")
elif(n1==n2 or n1==n3 or n2==n1 or n2==n3 or n3==n1 or n3==n2):
    print("Todos os números são iguais!")
else:
   maior =  max(n1,n2,n3)
print(f"O maior número digitado é: {maior}")
