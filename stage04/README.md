# Etapa 04 - Análises com o Segundo Modelo Lógico

## Slides da Apresentação da Etapa
> https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/slides/slidesEtapa4.pdf

## Modelo Conceitual Atualizado

> ![ER](https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/assets/entidadeRelacionamento2.png)

## Modelos Lógicos Atualizados

modelo lógico SQL:
~~~
Estado(_UF_, Nome)

Cidade(_Nome_, _Estado_)
  Estado chave estrangeira -> Estado(UF)
  
Aeroporto(_Sigla_, Descricao, Cidade)
  Cidade chave estrangeira -> Cidade(Nome)
 
Periodo(_Id_,_Semana_,_Ano_)

Rota(_Id_, Origem, Destino, VoosTotais)
  Origem chave estrangeira -> Aeroporto(Sigla)
  Destino chave estrangeira -> Aeroporto(Sigla)
 
Voo(_Rota_, _Periodo_, Quantidade)
  Rota chave estrangeira -> Rota(Id)
  Periodo chave estrangeira -> Periodo(Id)
  
Casos(_Estado_, _Periodo_, NumCasos)
  Estado chave estrangeira -> Estado(Nome)
  Periodo chave estrangeira -> Periodo(Id)
~~~

## Programa de extração e conversão de dados atualizado
Para a atualização das tabelas da etapa 3, decidimos continuar utilizando o python localmente para extrair e converter os dados, para otimizar o tempo. Mesmo que algumas partes pudessem ser feitas no jupyter, iria demandar tempo extra para um tarefa não essencial. Os scripts utilizados para gerar as tabelas se encontram na pasta src. </br>
https://github.com/Desnord/ProjetoFinalMC536/tree/main/stage04/src

## Conjunto de queries de dois modelos
As queries geradas para a revisão da etapa 3 se encontram também na pasta src. Porém, elas também estão disponíveis em um notebook.</br>
Além disso, esse notebook contém diversos selects e views, que são utilizadas para análise de dados, gerando um csv que é utilizado no notebook de análises. </br> 
pasta scr: https://github.com/Desnord/ProjetoFinalMC536/tree/main/stage04/src </br>
notebook de queries (jupyter/binder): https://github.com/Desnord/ProjetoFinalMC536/tree/main/stage04/notebooks/queries.ipynb </br>
notebook de análises (colab): https://github.com/Desnord/ProjetoFinalMC536/tree/main/stage04/notebooks/analise.ipynb </br>

### cypher 

cria nós, cada aeroporto é um nó que possui sigla e o nome da cidade em que está localizado
~~~ cypher
LOAD CSV WITH HEADERS FROM 'https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/data/processed/aeroportoFINAL.csv' AS line
CREATE (:aeroporto {cidade: line.Cidade , sigla: line.Sigla})

MATCH (a:aeroporto)
RETURN a LIMIT 50
~~~

cria arestas, cada rota é uma aresta que liga dois aeroportos, e possui como atributo a quantidade de voos da rota
~~~ cypher
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/Desnord/ProjetoFinalMC536/main/stage04/data/processed/rota.csv' AS line
MATCH (a1:aeroporto {sigla:line.Origem})
MATCH (a2:aeroporto {sigla:line.Destino})
CREATE (a1)-[r:rota {total: line.VoosTotais}]->(a2)

MATCH p = ()-[r:rota]->() 
RETURN p LIMIT 5
~~~

## Bases de Dados
título da base | link | breve descrição
----- | ----- | -----
`voos no brasil` | https://www.anac.gov.br/assuntos/dados-e-estatisticas/historico-de-voos | `datasets com voos no brasil, por ano e mês`
`infogripe*` | http://info.gripe.fiocruz.br | `sistema de casos de gripe no brasil`


*Para estes dados, seria necessário baixar centenas de csvs pelo sistema do infogripe, pois o sistema não tem uma api de acesso direta aos dados.
Entretanto, encontramos um projeto de um grupo que já fez essa parte de juntar os dados de cada semana, para todos os anos e estados. Assim, utilizamos
o csv do repositório deles, que pode ser encontrado no link: https://github.com/belisards/srag_brasil/blob/master/data/casos_uf.csv ou também na pasta
external. </br>

## Arquivos de Dados
nome do arquivo | link | breve descrição
----- | ----- | -----
`aeroporto.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/data/interim/aeroporto.csv | `Arquivo CSV de aeroportos obtido na etapa 3.`
`cidade.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/data/interim/cidade.csv | `Arquivo CSV de cidades obtido na etapa 3.`
`01voosANO.csv` | https://drive.google.com/drive/folders/1W9NUGk94Ys2_5HG5TKvImnto6k3IUcuc?usp=sharing | `Drive com todos os CSVs de voos obtidos ao final da etapa 3, e que foram utilizados como base na etapa 4.`
`casos_uf.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/data/external/casos_uf.csv | `Arquivo CSV de casos, obtido a partir da fonte original, encontrado em outro projeto no github.`
`casos.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/data/interim/casos.csv | `Arquivo CSV de casos, obtido a partir do anterior, apos ser processado na etapa 3.`

> Arquivos Finais

nome do arquivo | link | breve descrição
----- | ----- | -----
`aeroportoFINAL.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/data/processed/aeroportoFINAL.csv | `csv final de aeroporto`
`cidadeFINAL.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/data/processed/cidadeFINAL.csv | `csv final de cidade`
`casosFINAL.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/data/processed/casosFINAL.csv | `csv final de casos`
`periodo.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/data/processed/periodo.csv | `csv de periodo`
`estado.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/data/processed/estado.csv | `csv de estado`
`rotaFINAL.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/data/processed/rota.csv | `csv final de rotas`
`vooFINAL.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/data/processed/voo.csv | `csv final de voos`
`analise.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/data/processed/analise.csv | `csv obtido em um select feito no notebook de queries`
