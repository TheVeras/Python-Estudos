import json
#Exercício 1: Criação do Arquivo JSON da Biblioteca

#Crie um arquivo chamado `biblioteca.json` que contenha as informações sobre uma biblioteca. 
#-O JSON deve incluir o nome da biblioteca, o endereço, o número de livros e os horários de funcionamento.
#- Escreva um código em Python que leia o arquivo `biblioteca.json` que você criou e armazene os dados em um dicionário.
with open("T:\\Cursos Livres\\9900306841_PYTHON_I_FUNDAMENTOS_T09112024\\Rodrigo Veras\\Pyhton I\\JSON\\biblioteca.json",mode="r",encoding="utf-8") as arquivo:
    leitor = json.load(arquivo)
#- Utilizando o dicionário, exiba o nome e o endereço da biblioteca.
print(f'Nome: {leitor["nome"]}\nEndereço: {leitor["endereco"]}')
    
#Exercício 2: Criação de um Dicionário de Contatos
print("______________________________________________________________")
#- Crie um dicionário chamado contatos que contenha três entradas. Cada entrada deve ter um nome como chave e um número de telefone como valor.
#- Escreva um código em Python que adicione um novo contato ao dicionário contatos.
with open("T:\\Cursos Livres\\9900306841_PYTHON_I_FUNDAMENTOS_T09112024\\Rodrigo Veras\\Pyhton I\\JSON\\contatos.json","r",encoding="utf-8") as contato:
    data = json.load(contato)
    data ["Jeremias"] = "(11)913827563"
    data ["Elaine"] = "(11)964736436"
    
with open("T:\\Cursos Livres\\9900306841_PYTHON_I_FUNDAMENTOS_T09112024\\Rodrigo Veras\\Pyhton I\\JSON\\contatos.json","w",encoding="utf-8") as novo_contato:
        data_json = json.dump(data, novo_contato, ensure_ascii=False, indent=4)

#- Utilizando o dicionário contatos, exiba todos os nomes e números de telefone formatados como "Nome: Número".

for linha in data:
    print(linha, data[linha])

#Exercício 3: Criação do Arquivo JSON de Autor e Obra
print("______________________________________________________________")
#- Crie um arquivo chamado autor.json que contenha informações sobre um autor. O JSON deve incluir o nome do autor, a nacionalidade, a data de nascimento e as informações de uma obra, que deve conter o título e o ano de publicação.
#- Escreva um código em Python que leia o arquivo autor.json que você criou e armazene os dados em um dicionário.
with open("T:\\Cursos Livres\\9900306841_PYTHON_I_FUNDAMENTOS_T09112024\\Rodrigo Veras\\Pyhton I\\JSON\\autor.json","r",encoding="utf-8") as autor:
    autor_json = json.load(autor)
#- Utilizando o dicionário, exiba o nome do autor, a nacionalidade e as informações da obra (título e ano de publicação).
    for linha in autor_json:
        print(linha, autor_json[linha])