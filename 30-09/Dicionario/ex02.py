'''
Crie um programa que mostre um menu ao usuário com as
seguintes opções:
1 – Pesquisar
2 – Cadastrar
3 – Editar
4 – Excluir
5 – Exibir cadastros
6 – Sair
'''
opcoes = {
    1 : 'Pesquisar',
    2 : 'Cadastrar',
    3 : 'Editar',
    4 : 'Excluir',
    5 : 'Exibir cadastros',
    6 : 'Sair'
}
for c,v in opcoes.items():
    print(f'{c} - {v}')