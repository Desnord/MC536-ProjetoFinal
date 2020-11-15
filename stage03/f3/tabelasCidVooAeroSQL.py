import pandas as pd
import numpy as np

''' Tabela Cidade '''
# abre csv de cidade
cidade = pd.read_csv("cidades01.csv")
# exclui cidades duplicadas
cidade = cidade.drop_duplicates()

# separa dados por colunas, e transforma em lista padrao do python
estado = cidade['UF'].tolist()
nome = cidade['Cidade'].tolist()

# cria query de insercao
f = open("cidadeSQL.csv", "a")
f.write("Estado, Nome \n")

for i in range(len(nome)):
    strcid = "'{}', '{}'\n".format(nome[i], estado[i])
    f.write(strcid)
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

# cria csv final
f = open("aeroSQL.csv", "a")
f.write("Sigla, Descricao, Cidade \n")

for i in range(len(sigla)):
    straero = "'{}', '{}', '{}' \n".format(sigla[i], descricao[i], cidade[i])
    f.write(straero)
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

    # trabalha partida e chegada, retira horários, pois não nos é necessário
    partida = voos['Partida'].tolist()
    for i in range(len(partida)):
        partida[i] = partida[i].split()

    chegada = voos['Chegada'].tolist()
    for i in range(len(chegada)):
        chegada[i] = chegada[i].split()

    # cria csv final
    f = open("voosSQL"+str(ano)+".csv", "a")
    f.write("Origem, Destino, Partida, Chegada \n")

    for i in range(len(origem)):
        if(origem[i] in sigla and destino[i] in sigla):
            strvoo = "'{}', '{}', {}, {} \n".format(origem[i], destino[i], partida[i], chegada[i])
            f.write(strvoo)
    f.close()

