# Break é utilizado para interromper a execução de um loop
'''for i in range (1,11):
    if i == 5:
        break
    print(i)
#Continue faz co que o loop pule a execução do bloco de codigo e vá diretamento para a proxima iteração
for i in range(1,6):
    if i == 3:
        continue
    print(i)

# vamos criar um codigo que encontre e imprima o primeiro numero divisivel por 7. se encontrar um o loop deve parar
numeros = [12,18,24,35,42,55]
for numero in numeros:
    if numero % 7 == 0 :
        print(f'O primeiro numero divisivel por 7 é {numero}')
        break
    print(f'{numero} não é divisivel por 7')

# vamos criar um codigo que percorra uma lista de numeros e imprima apaneas numeros pares ignorando os impares
numeros = [1,2,3,4,5,6,7,8]

for num in numeros:
    if num % 2 != 0:
        continue
    print(f'Numero par: {num}')'''

#1 - Escreva um código que percorra uma lista de números e encontre o primeiro número negativo. 
# Quando o número for encontrado, o loop deve parar.
numeros = [10,29,38,13,51,32,-5,12,-4]
for num in numeros:
    if num < 0 :
        print(f'{num} é o primeiro numero negativo')
        break
    print(f'{num} não é um número negativo')
print('____________________________________')
#2 - Escreva  um código que some apenas os números positivos de uma lista. Se o número for negativo, o loop deve ignorá-lo e continuar.
soma = 0
for num in numeros:
    if num < 0 :
        continue
    soma+=num
    print(num)
print(f'A soma dos numeros positivos é: {soma}')
print('____________________________________')
#3 - Escreva um código que percorra uma lista de números e pare de executar assim que encontrar um número maior que 50.
for num in numeros:
    if num > 50:
        print(f'{num} é maior que 50')
        break
    print(num)