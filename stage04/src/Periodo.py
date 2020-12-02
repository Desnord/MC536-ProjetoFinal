# gera csv de periodo e sql de periodo

csv = open("periodo.csv", "a")
sql = open("periodo.sql", "a")
cont = 0

csv.write("Id,Semana,Ano\n")

for ano in range(2010,2020,1):
    for semana in range(1,53,1):

        # csv de periodo
        strDados = "{},{},{}\n".format(cont, semana, ano)
        csv.write(strDados)

        # sql de periodo
        strDados = "Insert Into Periodo (Id, Semana, Ano) Values ({}, {}, {});\n".format(cont, semana, ano)
        sql.write(strDados)

        cont += 1
csv.close()
sql.close()
