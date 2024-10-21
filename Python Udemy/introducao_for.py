'''
For + Range
range -> range(start, stop, step)

Iterável -> str, range, etc (__iter__)
Iterador -> quem sbae entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue o seu iterador
'''
numeros = range(0,100,2)

for par in numeros:
   print(par)

exemplo = iter('Rodrigo') #__iter__()
print(next(exemplo)) # saida R

# for letra in texto
texto = 'Exemplo' # iteravel
iterador = iter(texto) # iterador
'''
while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

Tudo isso é a mesma coisa que
'''
for letra in texto:
    print(letra)

########################################

for i in range(10):
    if i == 2:
        print('i é 2 , pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range (1,3):
        print(i,j)

else:
    print('For compeleto com sucesso!')
