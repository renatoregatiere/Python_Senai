pc = {
    'Processador':'Intel core ',
    'Memória':'8gb DDR4',
    'SSD':'250gb NVME',
    'Placa de video':'Radeon RX 6900'
}

del pc['Memória']
valor_excluido = pc.pop('SSD')
print(valor_excluido)
valor_excluido = pc.popitem()
print(valor_excluido)
print()
for c,v in pc.items():
    print(f'{c} -->{v}')