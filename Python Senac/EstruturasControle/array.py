'''
# Array [] é uma coleção ordenada de elementos
# Podem ser de qualquer tipo
frutas = ['maça', 'banana', 'laranja']
inteiros = [1, 2, 3, 4, 5] 
misturado = ['texto', 21, 45.5, True]
#pegando os valores de acordo com seu indice
fruta1 = frutas[0]
fruta2 = frutas[1]
#mostrando os valores atribuidos nas variaveis
print(fruta1)
print(fruta2)
print(frutas)
#modificando o valor no indice 0
frutas[0] = 'uva'
print(frutas)
#adicionando um novo valor ao final do array
frutas.append('abacaxi')
print(frutas)
#removendo um elemento
frutas.remove('banana')
frutas.pop() #remove o ultimo item
print(frutas)
#lista de numeros
numeros = [10, 20, 30, 40, 50]
print("Primeiro numero", numeros[0])
print(numeros)
#modificando um elemento
numeros[2] = 35
print(numeros)
#adicionando um elemento
numeros.append(60)
print(numeros)
#removendo um elemento
numeros.remove(35) #remove o numero 35
print(numeros)
#exibindo a quantidade de itens
print(len(numeros))
'''
#1  - Crie uma lista com cinco nomes de frutas. Em seguida, peça para eles realizarem as seguintes operações:
frutas = ['jaca', 'morango', 'goiaba', 'limão', 'abacate']
#a. Acessar e imprimir a segunda fruta da lista.
fruta2 = frutas[1]
print(fruta2)
#b. Substituir a última fruta por outra de sua escolha.
frutas[4] = 'mamão'
#c. Adicionar uma nova fruta ao final da lista.
frutas.append('manga')
#d. Remover a primeira fruta da lista.
frutas.pop(0)
print(frutas)

#2 - Crie uma lista com cinco nomes de pessoas. Em seguida, realize as seguintes operações:
nomes = ['Mariana', 'Maria', 'Mario', 'Manoela', 'Manoel']
#a. Adicione dois novos nomes ao final da lista.
nomes.append('Melissa')
nomes.append('Marcos')
#b. Substitua o segundo nome da lista por "Anônimo".
nomes[1] = 'Anônimo'
#c. Remova o primeiro nome da lista.
nomes.pop(0)
#d. Remova o último nome da lista.
nomes.pop()
print(nomes)

#3 - Crie uma lista com cinco itens que você compraria no supermercado. Em seguida, realize as seguintes operações:
compras = ['Café', 'Leite', 'Arroz', 'Azeite', 'Creme de Leite']
#a. Adicione dois novos itens ao final da lista.
compras.append('Macarrão')
compras.append('Feijão')
#b. Remova o primeiro item da lista.
compras.pop(0)
#c. Remova o último item da lista.
compras.pop()
#d. Adicione um novo item ao final da lista e remova o item "Leite" da lista.
compras.append('Molho de Tomate')
compras.remove('Leite')  
print(compras)
#4 - Crie uma lista com cinco números inteiros. Em seguida, realize as seguintes operações:
numeros = [10, 2, 1, 4, 9]
#a. Adicione um novo número ao final da lista.
numeros.append(6)
#b. Remova o menor número da lista.
import numpy as ny
numeros.remove(ny.min(numeros))
#c. Remova o último número da lista.
numeros.pop()
#d. Adicione um novo número ao final da lista e remova o primeiro número da lista.
numeros.append(8)
numeros.pop(0)
print(numeros)
    

