'''
Flag (bandeira) = marca um local
None = não valor
is e is not = é ou não é(tipo, valor, identidade)
id = identidade exemplo
v1 = 'a'
v2 = 'a'
# o python variaveis com valores iguals no mesmo local de memoria
print(id(v1))
print(id(v2))
#como  visto acima as duas variaveis possuiam o mesmo id

'''
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
