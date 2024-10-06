#1 - Solicite ao usuário que insira dois números inteiros. Subtraia o segundo número do primeiro e exiba o resultado.
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
sub = num1 - num2

print(f"o valor da subtração é {sub}")

#2 - Peça ao usuário que insira o valor total de uma compra e o valor pago. Calcule e exiba o troco a ser devolvido.
valor_compra = int(input("Digite o valor da compra: "))
valor_pago = int(input("Digite o valor pago: "))
troco = valor_pago - valor_compra

print(f"O valor do troco é: {troco}")

#3 - Solicite ao usuário que insira três números inteiros. Calcule a soma dos três números e exiba o resultado.
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))
som = num1 + num2 + num3

print(f"o valor da soma é {som}")

#4 - Peça ao usuário que insira as idades de duas pessoas. Calcule e exiba a diferença entre as idades.
idade1 = int(input("Digite a idade da primera pessoa: "))
idade2 = int(input("Digite a idade da segunda pessoa: "))
sub = idade1 - idade2 

print(f"A diferença de idade é: {sub} anos")
