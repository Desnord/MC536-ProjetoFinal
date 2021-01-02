# Etapa Final

## Projeto - `Análise de dados relacionados à gripe comum`

## Equipe `Glicemia`
* `Thomas Gomes Ferreira - 224919`
* `Pedro Jun Novais - 204878`

## Slides da Apresentação da Etapa Final

>   Quando apresentamos o trabalho, utilizamos o README.md da etapa 4: https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/README.md

## Resumo do Projeto
>   O projeto final da disciplina de banco de dados consiste em encontrar diversas fontes de dados, relacionados à um tema da saúde, com formatos diferentes e assim trabalhar para que possam ser interligados. E após isso, realizar algum tipo de análise. No nosso caso, trabalhamos com alguns dados que podem ser relacionados a gripe comum, e com isso realizamos a predição da quantidade de casos em um determinado estado e período. Além disso, as outras análises que foram feitas são visuais, exibindo dois gráficos que relacionam casos x período e voos x período, e os grafos de aeroportos e rotas.

## Motivação e Contexto
>   Escolhemos o tema da gripe para o projeto, por ser um assunto bem relevante na área da saúde e que pode se relacionar bem com diversos fatores. Assim é possível realizar uma proposta diversificada, além de facilitar a busca de dados de modelos variados. O vírus da gripe muda todo ano, sendo necessário desenvolvimento de vacinas para acompanhar o combate a doença. Assim, nossa motivação principal é a possibilidade de prever os casos de gripe esperados para determinado local e poder melhorar a profilaxia.

## Detalhamento do Projeto
> A partir do modelo relacional, um total de 3 análises foram feitas: Gráfico de voos x período, gráfico de casos x período e predição de casos. A geração dos gráficos foram simples de se elaborar, diferente do processamento dos dados. Apenas importamos os dados de 2 tabelas: analises.csv (obtida depois de diversos select's, views e joins que foram salvos depois de um select final) e estado.csv. Utilizando a biblioteca plotly geramos os gráficos e depois fizemos a predição de casos com um algoritmo de ML usando o sklearn. De forma resumida, temos os seguintes trechos de código:

importando dados (foram importados direto do github no notebook, para ambas as tabelas):
~~~python
url = "https://raw.githubusercontent.com/Desnord/ProjetoFinalMC536/main/stage04/data/processed/analise.csv"
data = requests.get(url).content
csv = pd.read_csv(io.StringIO(data.decode("utf-8")))
~~~

gerando gráfico (praticamente o mesmo codigo para ambos os gráficos):
~~~python
layout = go.Layout(
    title="casos de gripe no Brasil por período",
    xaxis=dict(title="periodo"),
    yaxis=dict(title="casos"),
    autosize=False,
    width=800,
    height=600,
    margin=go.layout.Margin(l=50,r=50,b=50,t=50,pad = 4)
)

fig = go.Figure(layout=layout) 

for estado in est['UF'].tolist():
  auxx = []
  auxy = []

  ctd=0
  for i in range(len(xlist)):
    if xlist[i][0] == estado:
      auxx.append(ctd)
      auxy.append(ylist[i])
      ctd+=1

  fig.add_trace(go.Scatter(x=auxx, y=auxy,mode='lines+markers', name=estado))
fig.show()
~~~

prevendo casos (utilizando machine learning):
~~~python
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

# arvore de decisao para predicao de casos
lg = DecisionTreeRegressor(random_state=0)
lg.fit(x_treino, y_treino)

ypred = lg.predict(x_teste)

r2 = r2_score(y_teste,ypred)
~~~
Por fim, o código completo dessas análises pode ser encontrado no notebook a seguir (utilizamos o colab):
https://github.com/Desnord/ProjetoFinalMC536/blob/main/Etapa%20Final/notebooks/analise.ipynb

> Para a parte do cypher, realizamos as queries de pagerank e community, e elaboramos uma imagem representando essa análise. A imagem foi gerada utilizando javascript/css/html, com um template do neovis. Esse template se encontra na pasta src, e há uma breve explicação no readme dentro da pasta: 
https://github.com/Desnord/ProjetoFinalMC536/blob/main/Etapa%20Final/src/visualgraphs.html

## Evolução do Projeto

<div align="center"><h2> Stage02</h2></div>
Esse estágio serviu apenas para decidir o assunto a ser trabalhado, análises planejadas para serem feitas e algumas fontes de dados que poderiam ser utilizadas no projeto.
</br>
</br>
<div align="center"><h2> Stage03</h2></div>
Nessa etapa, escolhemos as duas fontes de dados que utilizamos em todo o projeto. De forma resumida, uma das fontes possuia os casos de gripe e a outra os dados de voos e cidades. Além disso, foi nessa etapa que foi escolhido o segundo modelo lógico, que foi o modelo de grafos. Após escolher as fontes, iniciamos o processamento dos dados para interligá-los.

### Modelo Entidade Relacionamento
![ER1](https://github.com/Desnord/ProjetoFinalMC536/blob/main/Etapa%20Final/assets/entidadeRelacionamento1.png)

### Modelo Lógico
~~~
Estado(_UF_, Nome)

Cidade(_Nome_, _Estado_)
  Estado chave estrangeira -> Estado(UF)
  
Aeroporto(_Sigla_, Descricao, Cidade)
  Cidade chave estrangeira -> Cidade(Nome)
  
Voo(_VooID_, Partida, Chegada, Origem, Destino)
  Rota chave estrangeira -> Aeroporto(_Sigla_)
  Periodo chave estrangeira -> Aeroporto(_Sigla_)
  
Casos(_Estado_, _Semana_, _Ano_, NumCasos)
  Estado chave estrangeira -> Estado(Nome)
  Periodo chave estrangeira -> Periodo(Id)
~~~

### Processamento dos dados
Todos as fontes de dados estavam apresentadas através de arquivos csv. Baixamos os arquivos e processamos os dados através de scripts python e utilizando o Orange. Até aqui, não conseguimos implementar tudo que gostariamos, e tivemos alguns problemas com a interligação dos dados, que foi revisada e completada na etapa 4. O principal problema, estava com a tabela de voos, que possuia um volume muito grande de dados. 

### Queries realizadas
Algumas queries foram feitas nessa etapa, porém nenhuma análise foi feita com elas. Apenas para deixar como exemplo, uma das queries feitas foi a seguinte:

~~~sql
SELECT v.VooID, v.Origem, v.Destino, v.Partida, v.Chegada 
       FROM Voo v, Aeroporto aero, Cidade cid
       WHERE v.Destino = aero.Sigla and aero.Cidade = cid.Nome and cid.Estado = 'SP';	
~~~

### Considerações sobre essa etapa
De modo geral, conseguimos direcionar o projeto da forma que gostariamos, apesar dos problemas encontrados. Para a etapa 4, continuamos o que foi feito na etapa 3, complementando e adicionando o que fosse necessário. Assim, arrumamos o problema da tabela de voos, e realizamos as análises desejadas desde o começo do projeto, com sucesso. 

</br>
</br>
<div align="center"><h2> Stage04 e Final</h2></div>
Na etapa 4 revisamos e terminamos o processamento iniciado na etapa 3, obtendo as análises desejadas com o modelo relacional: gráficos e predição de casos. Além disso, implementamos um segundo modelo, o de grafos, atráves do neo4j/cypher. Com esse segundo modelo, realizamos uma análise visual de alguns dados.

## Processamento dos dados
Para processar os dados, continuamos do final da etapa 3 e utilizamos scripts python para processar os últimos csvs obtidos até então. Aqui, acrescentamos duas tabelas a fim de reduzir o volume de dados de voos, no caso, as tabelas periodo e rota. Com a tabela de periodo, ao invés de exibir os dados por dia e ano, agrupamos todos os voos por semana e separamos por rota. Assim, cada voo é uma rota que ocorre em um período, e possui uma quantidade de ocorrências.

### Modelo Entidade Relacionamento
O modelo entidade relacionamento foi revisado em conjunto com o modelo lógico, a fim de resolver os problemas encontrados com a tabela de voos:
![ER2](https://github.com/Desnord/ProjetoFinalMC536/blob/main/Etapa%20Final/assets/entidadeRelacionamento2.png)

### Modelo Lógico
Aqui o modelo lógico final foi obtido, em que foram adicionados duas tabelas em comparação com o modelo da etapa 3, além de alterar as tabelas já existentes. Com esse modelo, foi possível reduzir a tabela de voos que tinha ~10 milhões de linhas, para apenas ~3500 linhas, perdendo apenas um pouco de informação.

## Resultados e Discussão

Os resultados podem ser utilizados para se tirar conclusões a respeito da gripe, dado que as cidades com mais voos são cidades mais importantes e consequentemente terão mais casos registrados. Porém acreditamos que os fatores levados em consideração ainda são poucos e muito simples para serem utilizados como ferramenta prática de profilaxia. Assim, seriam necessários considerar mais dados (como clima, estatísticas de turismo, voos estrangeiros, rotas de outros tipos de transportes, campanhas de prevenção, etc) e realizar um estudo mais profundo. 
Temos os resultados das análises finais representados nas imagens à seguir:

Gráfico 1: Casos x Período </br>
![G1](https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/assets/grafico1.png)

Gráfico 2: Voos x Período </br>
![G2](https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/assets/grafico2.png)

Em seguida, temos a predição dos casos, que utilizou apenas o csv de analise. Com o modelo de regressão DecisionTreeRegressor do sklearn (ML), treinamos os dados de análise para realizar a predição dos casos em determinados período e estado. Obtemos uma confiabilidade de aproximadamente 92% com esse modelo, ou seja, o erro é bem pequeno ao prever casos e dado as limitações do trabalho, o resultado é bem satisfatório. Para realizar uma predição, fornecemos como entrada: um período (ano e semana), estado e quantidade de voo. Depois, atráves do modelo treinado, é feita a predição da quantidade de casos aproximados para a gripe comum. 

Exemplo para predição: </br>
![PRED](https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/assets/predicao.png)

Como resultado das análises em cypher (pagerank e community), obtivemos o seguinte grafo, com todos os aeroportos e rotas representados. A primeira imagem contém todo o grafo, com todos os aeroportos e rotas sendo representados na figura. Como o grafo é muito grande, colocamos uma segunda imagem com apenas uma amostra do grafo, em que podemos ver com clareza o resultado das análises feitas. Além disso, essas imagens foram obtidas com o neovis.js, uma biblioteca do javascript que pode ser facilmente interligada ao neo4j para obter imagens de grafos.
Nas imagens temos:
as comunidades representadas por cores;
a espessura das arestas de acordo com a quantidade de voos realizados naquela rota (quanto maior, mais voos foram feitos);
o tamanho dos nós de acordo com a relevância do aeroporto, obtido com o cálculo do pagerank (quanto maior o nó, maior a relevância do aeroporto);
</br>
Imagem com todo o grafo: </br>
![PCT1](https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/assets/pagerankcommunity.png) </br>

Imagem com uma pequena parte do grafo: </br>
![PCT2](https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/assets/pagerankcommunity2.png) </br>

## Conclusões
    De modo geral, conseguimos direcionar o projeto da forma que gostariamos, apesar dos problemas encontrados. Assim, arrumamos todos os problemas encontrados, e realizamos as análises desejadas desde o começo do projeto de forma satisfatória dentre os objetivos da disciplina. Na questão de aprendizado, diversos fatores podem ser levados em conta:
 - utilizamos diversas tecnlogias e conhecimentos no projeto (SQL, neo4j, jupiter, colab, javascript, html, markdown, python, etc)
 - utilizamos modelos de dados diversos (arquivos com csv's, relacional com sql, e grafos com cypher)
 - iniciar um projeto do zero, de forma praticamente livre (foi um desafio, pois não havia um ponto de partida para as análises e tivemos de usar de criatividade para tal)
 - processar dados diversos e interligá-los, apesar de que estes não possuiam nenhuma relação (aprendemos a lidar melhor com a criação de integrações)

## Modelo Conceitual Final

> ![ER Final](https://github.com/Desnord/ProjetoFinalMC536/blob/main/Etapa%20Final/assets/entidadeRelacionamento2.png)

## Modelos Lógicos Finais

Modelo Relacional:
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

Modelo de Grafos (Criamos os nós e arestas do grafo, com as queries em cypher a seguir e em seguida temos uma pequena amostra do grafo):
~~~ cypher
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/Desnord/ProjetoFinalMC536/main/stage04/data/processed/aeroportoFINAL.csv' AS line
CREATE (:aeroporto {cidade: line.Cidade , sigla: line.Sigla})
~~~

~~~ cypher
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/Desnord/ProjetoFinalMC536/main/stage04/data/processed/rota.csv' AS line
MATCH (a1:aeroporto {sigla:line.Origem})
MATCH (a2:aeroporto {sigla:line.Destino})
CREATE (a1)-[r:rota {total: toInt(line.VoosTotais)}]->(a2)
~~~

![AR1](https://github.com/Desnord/ProjetoFinalMC536/blob/main/Etapa%20Final/assets/aeroportosErotas.png)

## Programa de extração e conversão de dados atualizado
>   Os scripts python utilizados para conversão dos dados se encontra na pasta src: https://github.com/Desnord/ProjetoFinalMC536/tree/main/Etapa%20Final/src
>   Além disso, foram geradas duas tabelas extras, uma proveniente das queries em SQL, e outra das queries em Cypher.

## Conjunto de queries para todos os modelos

> queries SQL em notebook:

>> https://github.com/Desnord/ProjetoFinalMC536/blob/main/Etapa%20Final/notebooks/queries.ipynb

> queries em cypher:

>> Aqui geramos o pagerank dos aeroportos com pesos (total de voos)
gera grafo do pagerank
~~~ cypher
CALL gds.graph.create('prRotas','aeroporto','rota',{relationshipProperties: 'total'})
~~~
calcula e exibe pontuação para cada aeroporto
~~~ cypher
CALL gds.pageRank.stream('prRotas',{relationshipWeightProperty: 'total'})
YIELD nodeId, score 
RETURN gds.util.asNode(nodeId).sigla AS sigla, gds.util.asNode(nodeId).cidade AS cidade, score AS pontuacao
ORDER BY pontuacao DESC
~~~
calcula e armazena pontuacao em cada aeroporto
~~~ cypher
CALL gds.pageRank.stream('prRotas',{relationshipWeightProperty: 'total'})
YIELD nodeId, score
MATCH (a:aeroporto {sigla: gds.util.asNode(nodeId).sigla})
SET a.prscore = score
~~~

>> Tabém geramos as comunidades dos aeroportos
gera grafo das comunidades
~~~ cypher
CALL gds.graph.create('comunidade','aeroporto','rota')
~~~

obtem e exibe comunidades
~~~ cypher
CALL gds.louvain.stream('comunidade')
YIELD nodeId, communityId
RETURN gds.util.asNode(nodeId).sigla AS sigla, communityId
ORDER BY sigla DESC
~~~

obtem comunidades e armazenas ids nos aeroportos
~~~ cypher
CALL gds.louvain.stream('comunidade')
YIELD nodeId, communityId
MATCH (a:aeroporto {sigla: gds.util.asNode(nodeId).sigla})
SET a.comunidade = communityId
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

> Arquivos Intermediários

nome do arquivo | link | breve descrição
----- | ----- | -----
`aeroporto.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/Etapa%20Final/data/interim/aeroporto.csv | `Arquivo CSV de aeroportos obtido na etapa 3.`
`cidade.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/Etapa%20Final/data/interim/cidade.csv | `Arquivo CSV de cidades obtido na etapa 3.`
`01voosANO.csv` | https://drive.google.com/drive/folders/1W9NUGk94Ys2_5HG5TKvImnto6k3IUcuc?usp=sharing | `Drive com todos os CSVs de voos obtidos ao final da etapa 3, e que foram utilizados como base na etapa 4.`
`casos_uf.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/Etapa%20Final/data/external/casos_uf.csv | `Arquivo CSV de casos, obtido a partir da fonte original, encontrado em outro projeto no github.`
`casos.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/Etapa%20Final/data/interim/casos.csv | `Arquivo CSV de casos, obtido a partir do anterior, apos ser processado na etapa 3.`

> Arquivos Finais

nome do arquivo | link | breve descrição
----- | ----- | -----
`aeroportoFINAL.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/Etapa%20Final/data/processed/aeroportoFINAL.csv | `csv final de aeroporto`
`cidadeFINAL.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/Etapa%20Final/data/processed/cidadeFINAL.csv | `csv final de cidade`
`casosFINAL.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/Etapa%20Final/data/processed/casosFINAL.csv | `csv final de casos`
`periodo.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/Etapa%20Final/data/processed/periodo.csv | `csv de periodo`
`estado.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/Etapa%20Final/data/processed/estado.csv | `csv de estado`
`rotaFINAL.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/Etapa%20Final/data/processed/rota.csv | `csv final de rotas`
`vooFINAL.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/Etapa%20Final/data/processed/voo.csv | `csv final de voos`
`analise.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/Etapa%20Final/data/processed/analise.csv | `csv obtido em um select feito no notebook de queries`

nome do arquivo | link | breve descrição
----- | ----- | -----
`pagerankAeroportos.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/Etapa%20Final/data/processed/pagerankAeroportos.csv | `csv de pagerank dos aeroportos`
`comunidadesAeroportos.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/Etapa%20Final/data/processed/comunidadesAeroportos.csv | `csv de comunidades de aeroportos`
