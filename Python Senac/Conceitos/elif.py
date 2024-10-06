#1 - Escreva  um código que verifique se um número fornecido é positivo, negativo ou zero.

num = float(input("Digite o número: "))

if num < 0:
    print(f"Este número é negativo: {num}")
elif num == 0:
    print(f"Este número é ZERO: {num}")
else:
    print(f"este número é positivo: {num}")

#2 - Crie uma variável chamada `temperatura` e atribua a ela um valor numérico. 
# Depois, use as instruções `if`, `elif`, e `else` para decidir qual mensagem será exibida:

#- Se a temperatura for maior que 30, exiba "Está muito quente."
#- Se a temperatura for entre 20 e 30, exiba "O clima está agradável."
#- Se a temperatura for entre 10 e 19, exiba "Está um pouco frio."
#- Se a temperatura for menor que 10, exiba "Está muito frio."

temperatura = float(input("Digite a temperatuda: "))

if temperatura > 30:
    print(f"{temperatura}°C Está muito quente!")
elif temperatura > 19 and temperatura < 31:
    print(f"{temperatura}°C O clima ésta agradável.")
elif temperatura > 9 and temperatura < 20:
    print(f"{temperatura}°C Está um pouco frio.")
else:
    print(f"{temperatura}°C Está muito frio! ")

#3- Crie uma variável chamada `nota` e atribua a ela um valor numérico entre 0 e 100. 
# Depois, use as instruções `if`, `elif`, e `else` para determinar o seu desempenho:

#- Se a nota for maior ou igual a 90, exiba "Excelente".
#- Se a nota for entre 70 e 89, exiba "Bom".
#- Se a nota for entre 50 e 69, exiba "Regular".
#- Se a nota for menor que 50, exiba "Insuficiente"

nota = float(input("Digite o valor da nota: "))

if nota >= 90:
    print(f"{nota} Excelente!")
elif nota >=70 and nota < 90:
    print(f"{nota} Bom.")
elif nota >= 50 and nota < 70:
    print(f"{nota} regular.")
else:
    print(f"{nota} Insulficiente.")
    