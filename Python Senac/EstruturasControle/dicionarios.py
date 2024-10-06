'''#Dicionarios aramazenam dados em pares, chave e valor
# Usamos chaves {} e cada par de chave-valor é separado por dois pontos
aluno = {'nome':'joao', 'idade':31}

# crie um dicionario chamado pessoa com as informações nome, idade, e cidade, mostre o valor da chave nome
pessoa = {
    'nome':'Carlos',
    'idade':30,
    'cidade': 'São Paulo'
}
print(pessoa['nome'])
pessoa ['profissao'] = 'engenheiro'

print(pessoa)'''
#1 - Crie um dicionário chamado aluno com as chaves 'nome' e 'curso'. 
# Verifique se a chave 'idade' existe no dicionário. Se existir, mostre o valor correspondente. 
# Caso contrário, exiba uma mensagem dizendo que a chave não foi encontrada.
aluno = {
    'nome':'Rodrigo',
    'curso':'Python'
}
if 'idade' in  aluno:
    print(['idade'])
else:
    print('A chave não foi encontrada')
print('______________________')
#2 - Crie um dicionário chamado pessoa com as chaves 'nome', 'idade' e 'cidade'. 
# Em seguida, remova a chave 'cidade' do dicionário e mostre o dicionário atualizado.
pessoa = {
    'nome':'Rodrigo',
    'idade': 28,
    'cidade':'São Paulo'
}
print(pessoa)
pessoa.pop('cidade')
print(pessoa)
print('______________________')
#3 - Crie um dicionário chamado carro com as chaves 'marca', 'modelo' e 'ano'. 
# Em seguida, mostre todas as chaves e valores no formato "chave: valor" utilizando for.
carro = {
    'marca':'nissan',
    'modelo':'versa',
    'ano':2012
}
print(carro)
for item in carro:
    print(item,carro[item])

for chave, valor in carro.items():
    print(chave,':',valor)
print('______________________')
#4 - Crie um dicionário chamado familia que contenha dois dicionários internos, 
# um para pai (com as chaves 'nome' e 'idade') e outro para mãe (com as mesmas chaves). Em seguida, mostre o nome do pai e a idade da mãe.
familia = {
    'pai':{
        'nome':'Raimundo',
        'idade':59
    },
    'mae':{
        'nome':'Glair',
        'idade':61
    }
}
print(familia)
print(familia['pai']['nome'])
print(familia['mae']['idade'])
print('______________________')
#5 - Crie um dicionário chamado `estoque` onde as chaves são nomes de produtos 
# (por exemplo, `'camiseta'` e `'calça'`). Cada produto deve ter uma lista como valor, 
# contendo a quantidade disponível e o preço do produto. Em seguida, mostre a quantidade disponível de um dos produtos.
estoque = {
    'camiseta':(30, 89.90),
    'relogio':(5, 599.90),
    'tenis':(12, 699.99),
    'calca':(30, 120.90)
}
print(estoque['tenis'][0])
print('______________________')
