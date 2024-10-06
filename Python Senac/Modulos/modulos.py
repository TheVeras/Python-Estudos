# Modulo é um arquivo que contém definições e instruções.
# Organização (para dividir o código em partes lógicas)
#Reutulização (usar o mesmo coódigo em diferentes projetos)

import math # funções matemáticas
import os # interage com o Sistema Operacional

from datetime import datetime

print(math.sqrt(16))#retorna a raiz quadrada
print(os.getcwd())#retorna o diretorio em que estamos

agora = datetime.now()
print(f'A hora atual é {agora}')
