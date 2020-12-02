import numpy as np
import pandas as pd

#----------------------------------------------------------------------------------------------#
#Para gerar a tabela de cidade, é necessário o csv cidade.csv (o ultimo da etapa 3)------------#
#----------------------------------------------------------------------------------------------#

cidade = pd.read_csv("cidade.csv")

# exclui aeroportos duplicados
cidade = cidade.drop_duplicates()

nome = cidade['UF'].tolist()
estado = cidade['Cidade'].tolist()

f = open("cidadeFINAL.csv", "a")
f.write("Nome,Estado\n")

for i in range(len(nome)):
    f.write(nome[i].strip() + ","+ estado[i].strip() + "\n")
f.close()


f = open("cidade.sql", "a")
for i in range(len(nome)):
    strDados = "Insert Into Cidade (Nome, Estado) Values ('{}', '{}');\n".format(nome[i].strip(),estado[i].strip())
    f.write(strDados)
f.close()