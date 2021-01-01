import numpy as np
import pandas as pd
import datetime

#Para gerar a tabela de voos, é necessário os csvs de voo 01vooANO.csv (ultimo da etapa 3), ---#
#o csv periodo.csv e o csv final de rotas------------------------------------------------------#
#----------------------------------------------------------------------------------------------#

# abre csv final de rotas
arq = open("rota.csv", "r")
arqLines = arq.readlines()

ids = list()
rotas = list()
flag = 0

for l in arqLines: 
    if flag == 0:
        flag = 1
    else:
        at = l.split()
        at = at[0].split(",")
        ids.append(at[0])
        rotas.append([at[1],at[2]])

# abre csv de periodo
periodo = pd.read_csv("periodo.csv")

idP = periodo['Id'].tolist()
semanaP = periodo['Semana'].tolist()
anoP = periodo['Ano'].tolist()

# cria csv de voos
aux = []
aux2 = []
aux3 = []

for ano in range(2010,2020,1):
    # abre csv de voos de cada ano
    voos = pd.read_csv("01voos"+str(ano)+".csv")

    # exclui voos duplicados (se houver)
    voos = voos.drop_duplicates()
    voos = voos[voos.Partida != '?']
    voos = voos[voos.Chegada != '?']
    print(str(ano))

    # separa colunas
    origem  = voos['Origem'].tolist()
    destino = voos['Destino'].tolist()
    chegada = voos['Chegada'].tolist()

    # separa horario e data (horario nao eh necessario)
    # separa ano/mes/dia descartando horario
    for i in range(len(chegada)):
        chegada[i] = chegada[i].split()
        chegada[i] = chegada[i][0]

    # para todas os voos do csv atual
    for i in range(len(chegada)):
        '''print(chegada[i])'''
        chegada[i] = chegada[i].split("-")
        '''print(chegada[i])
        chegada[i] = list(map(str, chegada[i]))
        print(chegada[i])'''

        # encontra periodo para inserir
        year = chegada[i][0]
        month = chegada[i][1]
        day = chegada[i][2]

        # transformar data atual para numero da semana do ano (uma das 52)
        semana = datetime.date(int(year), int(month), int(day)).isocalendar()[1]

        # casos so vao até a semana 52
        if semana == 53:
            semana = 52

        idRota = 0
        idPeriodo = 0

        # encontra o codigo da rota do voo atual
        for j in range(len(rotas)):
            if origem[i] == rotas[j][0] and destino[i] == rotas[j][1]:
                    idRota = ids[j]
                    break

        # encontra o codigo do periodo do voo atual
        for j in range(len(idP)):
            if ano == anoP[j] and semana == semanaP[j]:
                idPeriodo = idP[j]
                break
            
        # se esse voo ja aconteceu nesse periodo, aumenta a quantidade
        if idRota in aux and idPeriodo in aux2:
            for j in range(len(aux)):
                if aux[j] == idRota and aux2[j] == idPeriodo:
                    aux3[j] += 1
        # senao insere o novo voo
        else:
            aux.append(idRota)
            aux2.append(idPeriodo)
            aux3.append(1)


f = open("voo.csv", "a")
f.write("Rota,Periodo,Quantidade\n")

for i in range(len(aux)):
        a = str(aux[i])
        b = str(aux2[i])
        c = str(aux3[i])
        f.write(a+","+b+","+c+"\n")
f.close()

# cria sql de voos
f = open("voo.sql", "a")
cont = 0

for i in range(len(aux)):
        strDados = "Insert Into Voo (Rota, Periodo, Quantidade) Values ({}, {}, {});\n".format(aux[i],aux2[i],aux3[i])
        cont += 1
        f.write(strDados)
f.close()