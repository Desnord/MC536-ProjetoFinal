import numpy as np
import pandas as pd
#----------------------------------------------------------------------------------------------#
#Para gerar a tabela de casos, é necessário o csv casos.csv (o ultimo da etapa 3)--------------#
#e o csv periodo.csv --------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#

casos = pd.read_csv("casos.csv")

# exclui aeroportos duplicados
casos = casos.drop_duplicates()

ano = casos['Ano'].tolist()
semana = casos['Semana'].tolist()
num = casos['Casos'].tolist()
estado = casos['Estado'].tolist()

periodo = pd.read_csv("periodo.csv")
id = periodo['Id'].tolist()
semana2 = periodo['Semana'].tolist()
ano2 = periodo['Ano'].tolist()

aux = []
aux2 = []
aux3 = []

f = open("casosFINAL.csv", "a")
f.write("Estado,Periodo,NumCasos\n")
for i in range(len(ano)):
    for j in range(len(id)):
        if semana[i] == semana2[j] and ano[i] == ano2[j]:
            f.write(estado[i].strip() + "," + str(id[j]) + "," + str(num[i]) + "\n")

            aux.append(estado[i].strip())
            aux2.append(str(id[j]))
            aux3.append(str(num[i]))
            break
f.close()

f = open("casos.sql", "a")
for i in range(len(aux)):
    strDados = "Insert Into Casos (Estado, Periodo, NumCasos) Values ('{}', {}, {}); \n".format(aux[i],aux2[i],aux3[i])
    f.write(strDados)
f.close()