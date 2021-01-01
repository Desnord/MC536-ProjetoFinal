# Etapa Final

## Projeto `Análise de dados relacionados à gripe comum`

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
> Apresente aqui detalhes da análise. Nesta seção ou na seção de Resultados podem aparecer destaques de código como indicado a seguir. Note que foi usada uma técnica de highlight de código, que envolve colocar o nome da linguagem na abertura de um trecho com `~~~`, tal como `~~~python`.
> Os destaques de código devem ser trechos pequenos de poucas linhas, que estejam diretamente ligados a alguma explicação. Não utilize trechos extensos de código. Se algum código funcionar online (tal como um Jupyter Notebook), aqui pode haver links. No caso do Jupyter, preferencialmente para o Binder abrindo diretamente o notebook em questão.

~~~python
df = pd.read_excel("/content/drive/My Drive/Colab Notebooks/dataset.xlsx");
sns.set(color_codes=True);
sns.distplot(df.Hemoglobin);
plt.show();
~~~

## Evolução do Projeto
> Relatório de evolução, descrevendo as evoluções na modelagem do projeto, dificuldades enfrentadas, mudanças de rumo, melhorias e lições aprendidas. Referências aos diagramas, modelos e recortes de mudanças são bem-vindos.
> Podem ser apresentados destaques na evolução dos modelos conceitual e lógico. O modelo inicial e intermediários (quando relevantes) e explicação de refinamentos, mudanças ou evolução do projeto que fundamentaram as decisões.
> Relatar o processo para se alcançar os resultados é tão importante quanto os resultados.

## Resultados e Discussão
> Apresente os resultados da forma mais rica possível, com gráficos e tabelas. Mesmo que o seu código rode online em um notebook, copie para esta parte a figura estática. A referência a código e links para execução online pode ser feita aqui ou na seção de detalhamento do projeto (o que for mais pertinente).
> A discussão dos resultados também pode ser feita aqui na medida em que os resultados são apresentados ou em seção independente. Aspectos importantes a serem discutidos: É possível tirar conclusões dos resultados? Quais? Há indicações de direções para estudo? São necessários trabalhos mais profundos?

## Conclusões
> Apresente aqui as conclusões finais do trabalho e as lições aprendidas.

## Modelo Conceitual Final

> Coloque aqui a imagem do modelo conceitual final em ER ou UML, como o exemplo a seguir:
> ![ER Taxi](images/er-taxi.png)

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

> Coloque um link para o arquivo do notebook que executa a extração e conversão de dados. Ele estará dentro da pasta `notebook`. Se por alguma razão o código não for executável no Jupyter, coloque na pasta `src`. Se a extração e conversão envolverem queries executadas através de uma interface de um SGBD não executável no Jupyter, como o Cypher, apresente na forma de markdown.

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

nome do arquivo | link | breve descrição
----- | ----- | -----
`pagerankAeroportos.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/data/processed/pagerankAeroportos.csv | `csv de pagerank dos aeroportos`
`comunidadesAeroportos.csv` | https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/data/processed/comunidadesAeroportos.csv | `csv de comunidades de aeroportos`
