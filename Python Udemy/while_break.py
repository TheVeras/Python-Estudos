'''
Repetições
While(enquanto)
Executa uma ação enquanto determinada condição for verdadeira
'''
condicao = True
while condicao:#loop infinito
    nome  = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break
print('Fim do laço')

contador = 0

while contador <= 10:
    print(contador)
    contador += 1

print('Fim do Laço')
