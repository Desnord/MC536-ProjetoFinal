import pandas as pd
import numpy as np

''' Tabela Casos '''
# abre csv de cidade
casos = pd.read_csv("casos01.csv")


# separa dados por colunas, e transforma em lista padrao do python
estado = casos['Estado'].tolist()
ano = casos['Ano'].tolist()
semana = casos['Semana'].tolist()
numcasos = casos['Casos'].tolist()

# cria query de insercao
f = open("casosSQL.csv", "a")
f.write("Estado, Ano, Semana, NumCasos \n")

for i in range(len(estado)):
    strcid = "'{}', {}, {}, {} \n".format(estado[i], ano[i], semana[i], numcasos[i])
    f.write(strcid)
f.close()

