#For (Para) Resondavel por percorrer listas

compras = ['Café', 'Leite', 'Arroz', 'Azeite', 'Creme de Leite']

for produto in compras:
    print(produto)

numeros = [1, 2, 3, 4, 5]
novos_numeros = []

for num in numeros:
    novos_numeros.append(num*2)

print(numeros)
print(novos_numeros)

numeros = [4, 11, 15, 7, 21, 3]
cont = 0
for num in numeros:
    if num > 10:
        cont+=1

print(numeros)
print(f"Existem {cont} numeros maior que 10")

#FOR

#1 - Crie uma lista com seis números inteiros. 
# Em seguida, use um laço for para contar quantos números pares existem na lista e imprimir o resultado.

#2 - Crie uma lista com seis números inteiros. 
# Em seguida, use um laço for para somar todos os números da lista que são maiores que 5 e imprimir o resultado.

#3 - Crie uma lista com seis números inteiros. 
# Em seguida, use um laço for para contar quantos números ímpares existem na lista e imprimir o resultado.
