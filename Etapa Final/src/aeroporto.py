import numpy as np
import pandas as pd

#----------------------------------------------------------------------------------------------#
#Para gerar a tabela de aeroporto, é necessário o csv aeroporto.csv (o ultimo da etapa 3)------#
#----------------------------------------------------------------------------------------------#

aeros = pd.read_csv("aeroporto.csv")

# exclui aeroportos duplicados
aeros = aeros.drop_duplicates()

sigla = aeros['Sigla'].tolist()
descricao = aeros['Descricao'].tolist()
cidade = aeros['Cidade'].tolist()

f = open("aeroportoFINAL.csv", "a")
f.write("Sigla,Descricao,Cidade\n")

for i in range(len(sigla)):
    f.write(sigla[i].strip() + "," + descricao[i].strip() + "," + cidade[i].strip() + "\n")
f.close()

f = open("aeroporto.sql", "a")
for i in range(len(sigla)):
    strDados = "Insert Into Aeroporto (Estado, Periodo, NumCasos) Values ('{}', '{}', '{}'); \n".format(sigla[i].strip(),descricao[i].strip(),cidade[i].strip())
    f.write(strDados)
f.close()