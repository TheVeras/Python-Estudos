# Json é uma estrutura de dados, utilizada para transmitir informações entre servidor e cliente
# Ele usa pares "chave-valor" parecido com dicionario
#jsonlint.com site para validar jsons

import json

with open("T:\Cursos Livres\9900306841_PYTHON_I_FUNDAMENTOS_T09112024\Rodrigo Veras\Pyhton I\JSON\dados.json","r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
    print(dados)
    print(dados["nome"])