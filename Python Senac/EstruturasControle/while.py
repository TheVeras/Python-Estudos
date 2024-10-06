'''soma= 0
while soma < 100:
    numero = int(input('Digite o numero a somar: '))
    soma += numero
    print(f'Soma atual: {soma}')
print(f'A soma atingiu o limite {soma}')'''

#1 - Escreva um código que execute uma contagem regressiva de 10 a 1 e, ao final, exiba a mensagem "Olá mundo!".
cont = 10
while cont > 0:
    print(cont)
    cont-=1
print('Olá Mundo')
#2 - Peça ao usuário para adivinhar um número entre 1 e 20. O loop continuará até que o usuário acerte o número. 
# Informe ao usuário se o palpite foi maior ou menor que o número correto.
#**Dica:** Defina um número secreto e compare os palpites do usuário com esse número.
numero = 16
palpite = 0
while numero != palpite:
    palpite = int(input('Faça seu palpite de 1 a 20: '))
    if palpite < numero :
        print('o palpite foi menor que o numero')
    elif palpite > numero :
        print('o palpite foi maior que o numero')
print('Parabens vc acertou \nFIM')
#3 - Crie um programa que peça ao usuário para inserir notas (valores numéricos). 
# O programa deve continuar pedindo notas até que o usuário insira um valor negativo. Quando isso acontecer, o programa deve calcular e exibir a média das notas inseridas.
#**Dica:** Use um loop `while` para acumular as notas e contar quantas foram inseridas antes de calcular a média.
cont = 0
nota = 0
media = 0
while nota >= 0:
    nota = float(input('Digite uma nota: '))
    if nota > 0:
        media += nota
        cont+=1

if cont > 0:
    media = media/cont
    print(f'o valor da media é: {media}')
else:
    print('Nenhuma nota valida foi inserida')