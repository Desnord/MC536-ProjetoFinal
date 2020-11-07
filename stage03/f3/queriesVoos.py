import numpy as np
import pandas as pd

''' Tabela Cidade '''
# abre csv de cidade
cidade = pd.read_csv("cidades01.csv")

# exclui cidades duplicadas
cidade = cidade.drop_duplicates()

# separa dados por colunas, e transforma em lista padrao do python
estado = cidade['UF'].tolist()
nome = cidade['Cidade'].tolist()

# cria query de insercao
f = open("cidadeInsert.sql", "a")

for i in range(len(nome)):
    # Gera Query de Inserção Para Cidades
    strInsert = "INSERT INTO Cidade (Nome, Estado) VALUES ('{}', '{}'); \n".format(nome[i], estado[i])
    f.write(strInsert)
f.close()

''' Tabela Aeroportos '''
# abre csv de aeroportos
aeros = pd.read_csv("aeroportos01.csv")

# exclui aeroportos duplicados
aeros = aeros.drop_duplicates()

# separa dados por colunas, e transforma em lista padrao do python
sigla = aeros['Sigla'].tolist()
descricao = aeros['Descricao'].tolist()
cidade = aeros['Cidade'].tolist()

# cria query de insercao
f = open("aerosInsert.sql", "a")

for i in range(len(sigla)):
    # Gera Query de Inserção Para Aeroportos
    strInsert = "INSERT INTO Aeroporto (Sigla, Descricao, Cidade) VALUES ('{}', '{}', '{}'); \n".format(sigla[i], descricao[i], cidade[i])
    f.write(strInsert)
f.close()


''' Tabela Voos '''
for ano in range(2010,2020,1):
    # abre csv de voos de cada ano
    voos = pd.read_csv("01voos"+str(ano)+".csv")
    # exclui voos duplicados (se houver)
    voos = voos.drop_duplicates()
    # separa dados por colunas, e transforma em lista padrao do python
    origem  = voos['Origem'].tolist()
    destino = voos['Destino'].tolist()
    partida = voos['Partida'].tolist()
    chegada = voos['Chegada'].tolist()

    # cria query de insercao
    f = open("voosInsert"+str(ano)+".sql", "a")

    for i in range(len(origem)):
        # Gera Query de Inserção Para Voos
        if(origem[i] in sigla and destino[i] in sigla):
            strInsert = "INSERT INTO Voo (Origem, Destino, Partida, Chegada) VALUES ('{}', '{}', {}, {}); \n".format(origem[i], destino[i], partida[i], chegada[i])
            f.write(strInsert)
    f.close()