a = 'A'
b = 'B'
c = 1.1
# se quiser utilizar indices podemos, os parametros ficam como se fossem uma lista
string = 'a={nome1} b={nome2} c={nome3:.2f} {nome1}'
formato = string.format(
    nome1=a,  #ao nomear um parametro, a partir do mesmo
    nome2=b, #devemos nomear todos os demais
    nome3=c)
                               
print(formato)
