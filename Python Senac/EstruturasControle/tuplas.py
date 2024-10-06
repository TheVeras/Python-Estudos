# Tuplas são lista de itens que não pode ser alterados, são definidos com () e separada com virgula
# Util para quando queremos garantias que os dados permanceam os mesmos

frutas = ('maça', 'banana', 'laranja')
print(frutas[0])

animais = ('cachorro', 'gato', 'Coelho')
if 'gato' in animais:
    print('O gato está na lista')
else:
    print('o gato não está na lista')

#1 - Crie uma tupla com 5 cores diferentes. Em seguida, mostre a terceira cor da tupla.
cores = ('branco','preto','vermelho','azul','verde')
print(cores[2])
#2 - Crie uma tupla chamada numeros com os números 1, 2, 3, 4, 5. Agora, tente alterar o valor do segundo número para 10.
numeros = (1, 2, 3, 4, 5)
numeros [1] = 10 # dara erro, tuplas são imutaveis