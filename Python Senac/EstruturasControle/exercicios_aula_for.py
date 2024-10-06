# Crie uma lista com seis numeros inteiros. 
# Em seguida use um laço para contar quandos numeros pares existem na lista e imprima o resultado

numeros = [14, 28, 3, 48, 5, 6]
cont = 0
for num in numeros:
    if num % 2 == 0:
        cont += 1

print(f'A quantidade de numeros pares é {cont}')

# Crie uma lista com seis numeros inteiros. 
# Em seguida use um laço para somar todos os numeros da lista que são maiores que 5 e imprima o resultado
soma = 0
cont = 0
for num in numeros:
    if num > 5:
        cont+=1
        soma = soma + num
print(f'Existem {cont} numeros maiores que 5 e a soma deles é: {soma}')

# Crie uma lista com seis numeros inteiros. 
# Em seguida use um laço para contar quandos numeros impares existem na lista e imprima o resultado
cont = 0
for num in numeros:
    if num % 2 != 0:
        cont += 1

print(f'A quantidade de numeros pares é {cont}')