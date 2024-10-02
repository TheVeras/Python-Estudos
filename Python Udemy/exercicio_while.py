'''
Iterando strings com while
'''
nome =  'Rodrigo Veras'

novo_nome = ''
cont = 0
while cont < len(nome):
    letra = nome[cont]
    novo_nome += f'*{letra}'
    cont += 1
novo_nome += '*'
print(novo_nome )
