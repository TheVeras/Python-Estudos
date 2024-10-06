# valores separados por vírgula
import csv
#primeiro parametros é o caminho do arquivo
#mode='r' igual a read de leitura 
#newline = '' - quebra correta de linha
'''with open("T:\\Cursos Livres\\9900306841_PYTHON_I_FUNDAMENTOS_T09112024\\Rodrigo Veras\\Pyhton I\\CSV\\dados.csv", "r") as csvarquivo:
    leitor = csv.reader(csvarquivo, delimiter=",") #leitura dos dados
    for i, linha in enumerate(leitor):
        if i == 0:
            print("Cabeçalho: " + str(linha))
        else:
            print("Valor: " + str(linha))

with open("T:\Cursos Livres\9900306841_PYTHON_I_FUNDAMENTOS_T09112024\Rodrigo Veras\Pyhton I\CSV\dados.csv", mode="r",newline="",encoding="utf-8") as csvarquivo:
    leitor = csv.reader(csvarquivo) #leitura dos dados
    for linha in leitor:
        print(linha)
'''
### Exercício 1: Criação do Arquivo CSV de Produtos
#Crie um arquivo chamado `produtos.csv` que contenha informações sobre cinco produtos. 
# Cada linha deve ter as seguintes colunas: ID, Nome, Preço e Categoria.


### Exercício 2: Leitura do Arquivo CSV
#Escreva um código em Python que leia o arquivo `produtos.csv` que você criou e armazene os dados em uma lista de dicionários.
dic_produtos = []
with open ("T:\\Cursos Livres\\9900306841_PYTHON_I_FUNDAMENTOS_T09112024\\Rodrigo Veras\\Pyhton I\\CSV\\Produtos.csv",mode="r",encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        dic_produtos.append(linha)
print(dic_produtos)

print('________________________________________')
### Exercício 3: Exibindo Nomes dos Produtos
#Utilizando um loop `for`, exiba apenas os nomes de todos os produtos contidos no arquivo `produtos.csv`.
for i in dic_produtos:
    print(i[1])
'''
with open ("T:\\Cursos Livres\\9900306841_PYTHON_I_FUNDAMENTOS_T09112024\\Rodrigo Veras\\Pyhton I\\CSV\\Produtos.csv",mode="r",encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        dic_produtos.append(linha)
        print(linha['Nome'])#dictreader
'''
print('________________________________________')
### Exercício 4: Exibindo Produtos Acima de um Certo Preço
#Escreva um código que, usando um loop `for`, exiba os nomes e preços dos produtos que custam mais de R$ 10,00.
for item in dic_produtos:
    if item[2] == 'Preço':
        continue
    valor = float(item[2])
    if valor > 10:
        print(item[1], item[2])
print('________________________________________')
