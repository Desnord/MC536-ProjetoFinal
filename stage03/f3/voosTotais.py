'''Junta tabelas com os dados de voo por ano'''
'''Assim, teremos uma tabela com os dados de voo de cada ano'''

anoIn = 2010
anoFi = 2019
 
for ano in range(anoIn,anoFi+1,1):

    ftot = open("total"+str(ano)+".csv","a")

    for mes in range(1,13):

        strArq = str(ano)+chr(92)+str(mes).zfill(2)+"-"+str(ano)+".csv"
        print(strArq)
        f = open(strArq)
        
        for linha in f:
            if not linha.__contains__("ICAO Empresa Aerea") or mes == 1:
                ftot.write(linha)

        f.close() 

    ftot.close()