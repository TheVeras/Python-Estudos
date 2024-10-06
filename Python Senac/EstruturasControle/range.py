'''# range(valor fixo)
for i in range(5):
    print(i)
print('______________________')
# range(nicio, fim)
for i in range (2, 7):
    print(i)
print('______________________')
# range (inicio, fim, passo)
for i in range(0, 11, 2):
    print(i)'''
#1 - Escreva um código para imprimir a tabuada do 5, de 5 até 50, usando a função range().
mult = 5
for i in range(5,51):
    print(f'{mult} X {i} = {mult*i}')
print('______________________')
#2 - Faça uma contagem regressiva de 10 até 1. Use um laço for e a função range() para contar de 10 até 1 e imprimir cada número.
for i in range(10,0,-1):
    print(i)
print('______________________')
#3 - Escreva todos os números pares de 2 até 20. Use um laço for junto com a função range() para gerar e imprimir esses números.
for i in range(2,21,2):
    print(i)
print('______________________')
