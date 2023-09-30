'''
Faça um programa que receba um nome de foguete e gere uma contagem regressiva para seu lançamento. A contagem deve iniciar em 10 e finalizar em 1 e logo em seguida o programa deve imprimir na tela: 'lançamento do foguete{nome} iniciado!'. Usar time.sleep(1)
'''
import time as t
i=10
nomeFoguete = str(input('Digite o nome do foguete: '))

while(i>=1):
    print(i)
    i=i-1
    t.sleep(1)
print(f'Lançamento do fogute {nomeFoguete}!')