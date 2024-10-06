'''
#operações logicas

# and(e) todas as analises devem ser true 
# or(ou) pelo menos uma das analises devem ser true
# not (nao) se a condição for true ele retorna false

#1 - Crie um programa que peça ao usuário para digitar o preço de um produto e a quantidade comprada. 
#Verifique se o preço é maior que 50 reais e se a quantidade é maior que 10. 
#Se ambas as condições forem verdadeiras, exiba "Você recebe um desconto!".
#Caso contrário, exiba "Sem desconto disponível". Inclua o else em sua solução.
preco = float(input("Digite o valor do produto: "))
qtd = int(input("Digite a quantidade do produto: "))

if preco > 50 and qtd > 10:
    print("Você recebeu um desconto")
else:
    print("Sem desconto disponivel")
#2- Crie um programa que peça ao usuário para digitar a sua idade e se possui um código de desconto (sim/não). 
# Se a idade for maior que 50 ou se o usuário tiver um código de desconto, exiba a mensagem "Você tem direito ao desconto!". 
# Caso contrário, exiba "Sem desconto disponível". Inclua o else em sua solução.
idade = int(input("Digite sua idade: "))
desconto = input("Possui cupom de desconto? sim/nao: ")

if idade > 50 or desconto == 'sim':
    print("Você tem direito ao desconto!")
else:
    print("Sem desconto disponivel")
#3 - Crie um programa que peça ao usuário para digitar um nome de usuário. Verifique se o nome digitado não é "Joao". 
# Se a condição for verdadeira, exiba "Acesso permitido, [nome]!". Caso contrário, exiba "Joao não pode ser usado como nome de usuário". 
# Inclua o else em sua solução.
nome = input("Digite seu nome: ")

if not nome.lower() == 'Joao' and not nome.lower() == 'joão':
    print("Acesso permitido")
else:
    print("Joao não pode ser usado como nome de usuario")
'''

#4 - Crie um programa que peça ao usuário para digitar suas notas em três provas. 
# Verifique se todas as notas são 6 ou mais. Se forem, exiba "Você passou em todas as provas!". 
# Caso contrário, exiba "Você não passou em todas as provas". Inclua o else em sua solução.

nota1 = float(input("Digite a nota da prova 1: "))
nota2 = float(input("Digite a nota da prova 2: "))
nota3 = float(input("Digite a nota da prova 3: "))

if nota1 >= 6 and nota2 >= 6 and nota3 >= 6:
    print("Você passou em todas as provas!")
else:
    print("Você não passou em todas as provas")

#5 - Crie um programa que peça ao usuário para digitar seu nome e idade. 
# Verifique se o nome digitado não é "admin" ou se a idade é menor que 18. 
# Se qualquer uma das condições for verdadeira, exiba "Acesso negado". Caso contrário, exiba "Acesso permitido". 
# Inclua o else em sua solução.

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if not nome.lower() == "admin" or idade < 18:
    print("Acesso negado")
else: 
    print("Acesso permitido")
