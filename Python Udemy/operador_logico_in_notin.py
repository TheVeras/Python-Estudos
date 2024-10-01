# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5 6
# R O D R I G O 
#-7-6-5-4-3-2-1
nome = input(' Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')
# print(nome[2])
# print(nome[-5])
#print('o' in nome) #verificando se a letra o se encontra dentro de nome
#print('Ro' not in nome)# verificando se nao encontra o valor Ro em nome
if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
