soma=0
i = int(input('Inicio: '))
f = int(input('fim: '))
p = int(input('passo: '))

for c in range(i,f,p):
    print(c)
    soma+=p
print(f'FIM, a soma foi:{soma}')