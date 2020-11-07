import numpy as np
import pandas as pd

''' Tabela Casos '''
# abre csv de cidade
casos = pd.read_csv("casos01.csv")

# exclui cidades duplicadas
casos = casos.drop_duplicates()

# separa dados por colunas, e transforma em lista padrao do python
ano = casos['Ano'].tolist()
semana = casos['Semana'].tolist()
numcasos = casos['Casos'].tolist()
estado = casos['Estado'].tolist()

# cria query de insercao
f = open("casosInsert.sql", "a")

for i in range(len(estado)):
    # Gera Query de Inserção Para Casos
    strInsert = "INSERT INTO Casos (Estado, Ano, Semana, NumCasos) VALUES ('{}', {}, {}, {}); \n".format( estado[i], ano[i], semana[i], numcasos[i])
    f.write(strInsert)
f.close()

