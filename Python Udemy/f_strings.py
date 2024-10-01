'''
Formatação básica de strings
s - string
d - int
f - float
.<número de digitos>f
x ou X - hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - Direita
^ - centro
= - força o numero a a aparece antes dos zeros
Sinal - + ou -
ex.: 0>-100,.1f
Conversion flags - !r !s !a
'''
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{variavel:$^10}.')
print(f'{1000.4873648123746:+,.1f}')# o sinal de mais sinaliza pro python que eu quero que o mesmo mostre o sinal para numeros positivos
print(f'o hexadecimal de 1500 é {1500:08X}')
