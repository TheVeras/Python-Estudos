#1 - Crie um programa que peça ao usuário para digitar a sua idade e a idade de um amigo. 
# Verifique se as idades são iguais e, se forem, exiba a mensagem "Vocês têm a mesma idade".
idade1 = int(input("Digite sua idade: "))
idade2 = int(input("Digite a idade do(a) amigo(a): "))
if idade1 == idade2:
    print(f"Vocês tem a mesma idade: {idade1} anos")
else:
    print("Vocês não possuem idades iguais")

#2 - Crie um programa que peça ao usuário para digitar dois números. 
# Verifique se os números são diferentes e, se forem, exiba a mensagem "Os números são diferentes".
num1 = int(input("Por favor digite um numero sem casas decimais: "))
num2 = int(input("POr favor digite mais um numero sem casas decimais: "))

if num1 != num2:
    print(f"{num1} é diferente de {num2}")
else:
    print(f"{num1} é igual a {num2}")

#3- Crie um programa que peça ao usuário para digitar a sua altura e a altura de um amigo (em centímetros). 
# Verifique se a altura do usuário é maior que a do amigo e, se for, exiba a mensagem "Você é mais alto que seu amigo".
altura1 = float(input("Digite sua altura: "))
altura2 = float(input("Digite a altura do(a) amigo(a): "))
if altura1 > altura2:
    print(f"Você é mais alto que seu amigo(a)")
elif altura1 == altura2:
    print("Vocês possuem a mesma altura")
else:
    print("Você é mais baixo que seu amigo(a)")

#4-  Crie um programa que peça ao usuário para digitar a sua nota em uma prova e a nota mínima necessária para passar. 
# Verifique se a nota do usuário é menor que a nota mínima e, se for, exiba a mensagem "Você não passou na prova".
nota1 = float(input("Digite sua nota na prova: "))
nota_corte = float(input("Digite a nota de corte: "))

if nota1 < nota_corte:
    print("Você não passou na prova")
else:
    print(f"Parabens você foi passou na prova com a nota: {nota1}")

#1- Crie um programa que peça ao usuário para digitar um número inteiro. 
# O programa deve verificar se o número é par ou ímpar. Se o número for par, exiba a mensagem "O número é par". Caso contrário, exiba "O número é ímpar".
n1 = int(input("Por favor digite um numero sem casas decimais: "))

if n1 % 2 == 0:
    print(f"{n1} é um número par")
else:
    print(f"{n1} é um número impar")

#2 - Crie um programa que peça ao usuário para digitar sua idade. 
# O programa deve verificar se o usuário é maior de idade (18 anos ou mais). Se for, exiba a mensagem 
# "Você é maior de idade". Caso contrário, exiba "Você é menor de idade".
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
