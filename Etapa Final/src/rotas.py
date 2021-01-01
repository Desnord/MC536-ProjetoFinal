import numpy as np
import pandas as pd

#----------------------------------------------------------------------------------------------#
#Para gerar a tabela de rotas, é necessário os csvs de voo 01vooANO.csv e----------------------#
#o csv aeroporto.csv --------------------------------------------------------------------------#
#(os ultimos da etapa 3)-----------------------------------------------------------------------#

# abre csv de aeroportos
aeros = pd.read_csv("aeroporto.csv")

# exclui aeroportos duplicados
aeros = aeros.drop_duplicates()

# separa siglas existentes
sigla = aeros['Sigla'].tolist()

#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------#

''' Tabela Rota '''
# cria lista de rotas
rotas = list()
total = list()

for ano in range(2010,2020,1):
    # abre csv de voos de cada ano
    voos = pd.read_csv("01voos"+str(ano)+".csv")

    # exclui voos duplicados (se houver)
    voos = voos.drop_duplicates()
    voos = voos[voos.Partida != '?']
    print(str(ano))

    # separa colunas de origem e destino
    origem  = voos['Origem'].tolist()
    destino = voos['Destino'].tolist()
    
    # junta duplas em linhas, origem/destino
    for i in range(len(origem)):

        atual = [origem[i],destino[i]]

        if atual in rotas:
            for j in range(len(rotas)):
                if rotas[j] == atual:
                    total[j] += 1
                    break
        else:
            if atual[0] in sigla and atual[1] in sigla:
                rotas.append(atual)
                total.append(1)


# cria csv de rotas
f = open("rota.csv", "a")
f.write("Id,Origem,Destino,VoosTotais\n")
cont = 0

for i in range(len(rotas)):
        strDados = "{},{},{},{}\n".format(cont,rotas[i][0],rotas[i][1],total[i])
        f.write(strDados)
        cont += 1
f.close()

# cria sql de rotas
f = open("rota.sql", "a")
cont = 0
ids = []

for i in range(len(rotas)):
        strDados = "Insert Into Rota (Id, Origem, Destino, VoosTotais) Values ({}, '{}', '{}', {});\n".format(cont,rotas[i][0],rotas[i][1],total[i])
        ids.append(cont)
        cont += 1
        f.write(strDados)
f.close()