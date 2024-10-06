'''# funções são blocos de codigos que podem sser reeutilizados

#organização
#Manutenção de codigos com facilidade
#Reutilização

#def nome_da_funcao():
    #codigo da função

#def - palavra chave que defina a função
#() - podemos definir parametros(valores de entrada), se necessário
# : indica o inicio do bloco de codigo
def saudacao():
    print("Olá mundo")

saudacao()
saudacao()

def saudacao2(nome):
    print(f"Olá {nome}")

saudacao2('Rodrigo')

#def media(float(a),float(b)):
#    media = (a+b)/2
#    return media

def soma(a,b):
    return a + b

resultado_soma = soma(5,3)    
print(resultado_soma)'''

#1 - Crie uma função chamada par_ou_impar que recebe um número como parâmetro e verifica se ele é par ou ímpar. 
# A função deve imprimir "Par" se for par e "Ímpar" se for ímpar.
def par_ou_impar(num):
    if num % 2 == 0:
        print(f'O número {num} é par')
    else:
        print(f'O número {num} é impar')

# Testando a função
par_ou_impar(10)  # Saída: Par
par_ou_impar(7)   # Saída: Ímpar

print('_______________________________________')
#2 - Crie uma função chamada `calcular_media` que recebe três notas como parâmetros e retorna a média delas.
def calcular_media(n1, n2, n3):
    return (n1+n2+n3)/3

# Testando a função
resultado = calcular_media(8, 9, 7)
print(resultado)  # Saída: 8.0

print('_______________________________________')
#3 - Crie uma função chamada contar_letras que recebe uma string como parâmetro e retorna o número de letras dessa string.
def contar_letras(s):
    cont = 0
    for l in s:
        cont+=1
    return cont


# Testando a função
quantidade = contar_letras("Python")
print(quantidade)  # Saída: 6

print('_______________________________________')
#4 - Crie uma função chamada tabuada que recebe um número como parâmetro e imprime a tabuada de 1 a 10 desse número.
def tabuada(num):
    for i in range (1,11):
        print(f'{num}X{i}={num*i}')

# Testando a função
tabuada(5)
# Saída:
#5 x 1 = 5
#5 x 2 = 10
#5 x 3 = 15
#...
#5 x 10 = 50
print('_______________________________________')
#5 - Crie uma função chamada soma_lista que recebe uma lista de números como parâmetro e retorna a soma de todos os elementos dessa lista.
def soma_lista(lista):
    soma = 0
    for n in lista:
        soma+=n
    return soma
# Testando a função
numeros = [1, 2, 3, 4, 5]
resultado = soma_lista(numeros)
print(resultado)  # Saída: 15

print('_______________________________________')
#6 - Crie uma função chamada maior_numero que recebe uma lista de números como parâmetro e retorna o maior número dessa lista.
def maior_numero(lista):
    maior = 0
    for i in lista:
        if i > maior:
            maior = i
    return maior

# Testando a função
numeros = [10, 23, 5, 78, 4]
resultado = maior_numero(numeros)
print(resultado)  # Saída: 78

print('_______________________________________')
#7 - Crie uma função chamada soma_pares que recebe uma lista de números e retorna a soma de todos os números pares presentes na lista.
def soma_pares(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma+=i
    return soma

# Testando a função
numeros = [10, 21, 32, 43, 54]
resultado = soma_pares(numeros)
print(resultado)  # Saída: 96
print('_______________________________________')
