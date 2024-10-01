# 1 - Crie uma lista com seis números inteiros. 
# Em seguida, use um laço para  contar quantos números pares 
# existem na lista e impirma o resultado.
numeros = [14,28,3,48,5,6]
cont = 0
for num in numeros:
    if num % 2 == 0:
        cont += 1
print(f"A quantidade de números pares é {cont}")

# 2 - Crie uma lista com seis números inteiros. 
# Em seguida, use um laço para  somar todos os números 
# da lista que são maiores que 5 e impirma o resultado 
soma = 0
cont = 0
for num in numeros:
    if num > 5:
        cont+=1
        soma = soma + num

print(f"Existem {cont} números maiores que 5 e a soma dele é: {soma}")
# 3 - Crie uma lista com seis números inteiros. 
# Em seguida, use um laço para  contar quantos números ímpares 
# existem na lista e imprima o resultado.
cont = 0
for num in numeros:
    if num % 2 != 0:
        cont += 1
print(f"A quantidade de números ímpares é {cont}")
