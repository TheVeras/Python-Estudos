# Calculadora com While
while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou mais números digitados são inválidos: ')
        continue
    
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador Inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    resultado = None
    if operador == '+':
        resultado = num_1_float + num_2_float
        print(f'{num_1_float} + {num_2_float} = {resultado}')
    elif operador == '-':
        resultado = num_1_float - num_2_float
        print(f'{num_1_float} - {num_2_float} = {resultado}')
    elif operador == '/':
        resultado = num_1_float / num_2_float
        print(f'{num_1_float} / {num_2_float} = {resultado}')
    elif operador == '*':
       resultado = num_1_float * num_2_float
       print(f'{num_1_float} * {num_2_float} = {resultado}') 
    
    else:
        print('Algo de errado não está certo')
        print('O operador não pode ser vazio')
        continue

    sair = input('Deseja sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break

print('Fim')
