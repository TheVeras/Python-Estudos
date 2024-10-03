frase = 'O python é uma linguagem de programação '\
    'multiparadiogma. ' \
    'Python foi criado por Guido van Rossum.'

i = 0
qtd_ocorrencias = 0
letra = ''

while i < len(frase):
    letra_atual = frase[i]
    i += 1
    
    if letra_atual == ' ':
        continue

    qtd_ocorrencias_atual = frase.count(letra_atual)

    if qtd_ocorrencias  < qtd_ocorrencias_atual:
        qtd_ocorrencias = qtd_ocorrencias_atual
        letra = letra_atual
    
print(f'A letra com maior ocorrencia foi: "{letra}" com {qtd_ocorrencias}X')
