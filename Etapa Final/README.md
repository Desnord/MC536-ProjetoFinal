# Etapa Final

## Projeto `Análise de dados relacionados à gripe comum`

## Equipe `Glicemia`
* `Thomas Gomes Ferreira - 224919`
* `Pedro Jun Novais - 204878`

## Slides da Apresentação da Etapa Final

> Coloque um link para o arquivo dos slides da apresentação final que estão na pasta `slides`.

## Resumo do Projeto
> O projeto final da disciplina de banco de dados consiste em encontrar diversas fontes de dados, relacionados à um tema da saúde, com formatos diferentes e assim trabalhar para que possam ser interligados. E após isso, realizar algum tipo de análise. 
No nosso caso, trabalhamos com alguns dados que podem ser relacionados a gripe comum, e com isso realizamos a predição da quantidade de casos em um determinado estado e período. Além disso, as outras análises que foram feitas são visuais, exibindo dois gráficos que relacionam casos x período e voos x período, e os grafos de aeroportos e rotas. 

## Motivação e Contexto

> Descrição do tema do projeto, incluindo motivação e contexto gerador.

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

> Coloque aqui os modelos lógicos dos bancos de dados relacionados aos modelos conceituais. Todos os modelos lógicos da versão final devem estar presentes, mesmo que tenham sido apresentados em etapas anteriores. Para o modelo relacional, sugere-se o formato a seguir. Para outros modelos lógicos o formato é livre, pode ser adotado aqueles apresentados em sala.

> Exemplo de modelo lógico relacional
~~~
PESSOA(_Código_, Nome, Telefone)
ARMÁRIO(_Código_, Tamanho, Ocupante)
  Ocupante chave estrangeira -> PESSOA(Código)
~~~

## Programa de extração e conversão de dados atualizado

> Coloque um link para o arquivo do notebook que executa a extração e conversão de dados. Ele estará dentro da pasta `notebook`. Se por alguma razão o código não for executável no Jupyter, coloque na pasta `src`. Se a extração e conversão envolverem queries executadas através de uma interface de um SGBD não executável no Jupyter, como o Cypher, apresente na forma de markdown.

## Conjunto de queries para todos os modelos

> Acrescente um link para o(s) arquivo(s) do(s) notebook(s) que executa(m) as queries para cada um dos modelos lógicos. Eles estarão dentro da pasta `notebook`. Se por alguma razão o código não for executável no Jupyter, coloque na pasta `src`. Se as queries forem executadas através de uma interface de um SGBD não executável no Jupyter, como o Cypher, apresente na forma de markdown.
> Apresente todas as suas queries em versão final, mesmo que tenham aparecido em etapas anteriores.

## Bases de Dados
> Elencar as bases de dados utilizadas no projeto. Apresente todas as bases usadas na versão final, mesmo aquelas que tenham sido apresentadas em etapas anteriores.

título da base | link | breve descrição
----- | ----- | -----
`<título da base>` | `<link para a página da base>` | `<breve descrição da base>`

## Arquivos de Dados
> Elencar os arquivos usados no projeto que estão disponíveis no Github do projeto. Apresente todos os arquivos usados na versão final, mesmo aqueles que tenham sido apresentadas em etapas anteriores.

nome do arquivo | link | breve descrição
----- | ----- | -----
`<nome do arquivo>` | `<link para o arquivo>` | `<breve descrição do arquivo>`

> Os arquivos devem ser colocados na pasta `data`, em subpasta conforme seu papel (externo, interim, processado, raw). A diferença entre externo e raw é que o raw é em formato não adaptado para uso. A pasta `raw` é opcional, pois pode ser substituída pelo link para a base original da seção anterior.
> Coloque arquivos relacionais (usualmente CSV), XML ou JSON que não estejam disponíveis online e sejam acessados pelo notebook.


</br>
</br>
</br>
</br>
</br>
</br>
</br>
</br>
</br>
</br>
<div align="center"><h2> Stage02</h2></div>
Esse estágio serviu apenas para decidir o assunto a ser trabalhado, análises planejadas para serem feitas e algumas fontes de dados que poderiam ser utilizadas no projeto.
</br>
</br>
<div align="center"><h2> Stage03</h2></div>
Nessa etapa, escolhemos as duas fontes de dados que utilizamos em todo o projeto. De forma resumida, uma das fontes possuia os casos de gripe e a outra os dados de voos e cidades. Após escolher as fontes, iniciamos o processamento dos dados para interligá-los.

### Modelo Entidade Relacionamento
![ER1](https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/assets/entidadeRelacionamento1.png)

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
![ER2](https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/assets/entidadeRelacionamento2.png)

### Modelo Lógico
Esse foi o modelo lógico final obtido, em que foram adicionados duas tabelas, além de alterar as tabelas já existentes. Com esse modelo, foi possível reduzir a tabela de voos
que tinha ~10 milhões de linhas, para apenas ~3500 linhas, perdendo apenas um pouco de informação.

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

### Análises - Modelo Tabular (SQL)
Para realizar análises com o modelo tabular, criamos dois notebooks: analises e queries. No notebook de queries, inicialmente, criamos todas as tabelas em sql a partir dos csvs obtidos no processamento como o exemplo a seguir:

~~~sql
CREATE TABLE Estado
(
    UF VARCHAR(2) NOT NULL,
    Nome VARCHAR(40) NOT NULL,
    PRIMARY KEY(UF)
)
AS SELECT UF,Nome FROM CSVREAD('https://raw.githubusercontent.com/Desnord/ProjetoFinalMC536/main/stage04/data/processed/estado.csv');
~~~

Em seguida, realizamos diversos queries em sql com as mais diversas complexidades que trazem diversas informações interessantes, porém não foram utilizadas diretamente na análise final. A única query utilizada para obter os gráficos e a predição de casos foi a última do notebook, tal que as queries anteriores serviram como parte do raciocínio utilizado para se obtê-la, dado a sua alta complexidade. Como muitas queries foram feitas, listamos a seguir algumas delas, apenas como exemplo:

~~~sql
-- total de casos de gripe por estado, entre 2010 e 2019

select Estado, SUM(NumCasos) TotalDeCasos
from Casos
group by Estado;
~~~


~~~sql
-- estados do destino de cada rota

select r.Id, r.Destino, c.Estado
from Rota r, Aeroporto a, Cidade c
where r.Destino = a.Sigla and a.Cidade = c.Nome;
~~~

~~~sql
-- para todo estado, mostra a quantidade de voos naquele periodo

SELECT ep.estado, ep.periodo, coalesce(vei.qtd, 0) as qtd
FROM EstadoPeriodos as ep
LEFT JOIN VoosEstadoIncompleto as vei
on vei.periodo = ep.periodo and vei.estado = ep.estado;
~~~

E a seguir temos a última query, que é um select que foi feito a partir de uma view. Com ela, agrupamos os dados de voos e casos por periodo e estado, e em seguinda salvamos as informações em um csv (analise.csv):

~~~sql
-- seleciona estados, periodos (semana+ano), quantidade de voos realizados, quantidade de casos registrados

select aux.estado,p.semana,p.ano,aux.voos,aux.casos
from Periodo p, auxiliar2 aux
where aux.Periodo = p.Id;
~~~


Por fim, temos o resultado final dessa parte, que foi feito em um notebook de analises e utilizamos como base dois arquivos csv: estado.csv (tabela com todos os estados) e analise.csv (tabela obtida com o SGBD). Assim, realizamos análises visuais a partir desses dois csvs, com dois gráficos interativos. Para cada estado, os casos e voos são buscados e representados de acordo. O primeiro gráfico, apresenta as ocorrências de casos de gripe ao longo dos períodos, e o segundo apresenta as ocorrências de voos que chegam ao longo dos períodos. Através desses gráficos, é possível escolher quais estados mostrar as informações, exibindo por default todas as 27 curvas (26 estados + distrito federal). 

Gráfico 1: Casos x Período </br>
![G1](https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/assets/grafico1.png)

Gráfico 2: Voos x Período </br>
![G2](https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/assets/grafico2.png)

Em seguida, temos a predição dos casos, que utilizou apenas o csv de analise. Com o modelo de regressão DecisionTreeRegressor do sklearn (ML), treinamos os dados de análise para realizar a predição dos casos em determinados período e estado. Obtemos uma confiabilidade de aproximadamente 92% com esse modelo, ou seja, o erro é bem pequeno ao prever casos e dado as limitações do trabalho, o resultado é bem satisfatório. Para realizar uma predição, fornecemos como entrada: um período (ano e semana), estado e quantidade de voo. Depois, atráves do modelo treinado, é feita a predição da quantidade de casos aproximados para a gripe comum. 

Exemplo para predição: </br>
![PRED](https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/assets/predicao.png)

### Análises - Modelo De Grafos (Neo4j/Cypher)

> Criamos os nós e arestas do grafo, com as queries em cypher a seguir e em seguida temos uma pequena amostra do grafo:

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

![AR1](https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/assets/aeroportosErotas.png)


> Aqui geramos o pagerank dos aeroportos com pesos (total de voos):

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

> Tabém geramos as comunidades dos aeroportos:

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

Como resultado dessa análise, obtivemos o seguinte grafo, com todos os aeroportos e rotas representados. A primeira imagem contém todo o grafo, com todos os aeroportos e rotas sendo representados na figura. Como o grafo é muito grande, colocamos uma segunda imagem com apenas uma amostra do grafo, em que podemos ver com clareza o resultado das análises feitas. Além disso, essas imagens foram obtidas com o neovis.js, uma biblioteca do javascript que pode ser facilmente interligada ao neo4j para obter imagens de grafos.
Nas imagens temos:
as comunidades representadas por cores;
a espessura das arestas de acordo com a quantidade de voos realizados naquela rota (quanto maior, mais voos foram feitos);
o tamanho dos nós de acordo com a relevância do aeroporto, obtido com o cálculo do pagerank (quanto maior o nó, maior a relevância do aeroporto);
</br>
Imagem com todo o grafo: </br>
![PCT1](https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/assets/pagerankcommunity.png) </br>

Imagem com uma pequena parte do grafo: </br>
![PCT2](https://github.com/Desnord/ProjetoFinalMC536/blob/main/stage04/assets/pagerankcommunity2.png) </br>
