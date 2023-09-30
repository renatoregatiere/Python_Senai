contato = {
    'João':'joao.gomes@gmail.com',
    'Ana Rosa':'rosa.ana@terra.com.br',
    'Luis':'luis45@gmail.com'
}
nome = input('Digeite o nome a ser pesquisado: ')
if(nome in contato):
    print(f'Email do (a) {nome}: {contato[nome]}')
else:
    print(f'Contato {nome} não encontrado!')