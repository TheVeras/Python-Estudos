import requests

cnpj = input('Digite o cnpj da empresa desejada (apenas números): ')
url = f'https://receitaws.com.br/v1/cnpj/{cnpj}'

conexao = requests.get(url)

if conexao.status_code == 200:
    dados = conexao.json()
    print(f'Informações da empresa: {dados["fantasia"]}')
    print(f'Abertura: {dados["abertura"]}')
    print(f'Situação: {dados["situacao"]}')
    print(f'Nome: {dados["nome"]}')
    print(f'Fantasia: {dados["fantasia"]}')
    print(f'Atividade: {dados["atividade_principal"][0]["text"]}')
    print(f'CPNJ: {dados["cnpj"]}')
else:
    print('Erro de conexão')

