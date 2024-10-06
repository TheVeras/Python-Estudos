import json

with open("T:\Cursos Livres\9900306841_PYTHON_I_FUNDAMENTOS_T09112024\Rodrigo Veras\Pyhton I\JSON\lista.json","r", encoding="utf-8") as arquivo:
    lista = json.load(arquivo)
    print(lista)

