<div align="center"><h1> ProjetoFinalMC536 - Projeto final da disciplina de Banco de Dados </h1></div>
<div align="center"><h3> Grupo: </h3></div>
<div align="center"> Thomas Gomes Ferreira - 224919 </div>
<div align="center"> Pedro Jun Novais - 204878 </div>

## Introdução
Escolhemos o tema da gripe para o projeto, por ser um assunto bem relevante na área da saúde
e que pode se relacionar . Assim é possível realizar uma proposta diversificada, além de facilitar
a busca de dados de modelos variados. O vírus da gripe muda todo ano, sendo necessário desenvolvimento
de vacinas para acompanhar o combate a doença. Assim, nossa motivação principal é a possibilidade de
prever os casos de gripe esperados para determinado local e poder melhorar a profilaxia.

## Interligação, análise dos dados e resultados esperados
A pior parte do projeto está na interligação dos dados, já que originalmente não possuem
relações entre si. Assim, primeiro os dados serão convertidos para um único modelo lógico, 
na forma tabular. Esses dados tabulares serão preparados no Orange, e depois exportados
em csv. Com os arquivos .csv obtidos, realizaremos algumas análises em um programa em python.

A principal análise que será feita, envolve a predição de algo relacionado a gripe, como o número
de casos esperados para determinado país. Apesar disso, não sabemos se os dados são suficientes
para fazer essa predição. Talvez seja necessário buscar mais fontes, descartar algumas ou 
mudar qual a predição que será realizada. 

## Bases de Dados
Encontramos algumas bases de dados que podem ser utilizadas: </br>
-https://www.kaggle.com/volpatto/temperature-timeseries-for-some-brazilian-cities</br>
-https://www.fludb.org/brc/vaccineRecommend.spg?decorator=influenza</br>
-https://www.kaggle.com/ramirobentes/flights-in-brazil</br>
-https://www.paho.org/hq/index.php?option=com_topics&view=rdmore&cid=4302&item=influenza&type=statistics&Itemid=40753&lang=en</br>
-https://www.who.int/influenza/gisrs_laboratory/flunet/en/</br>

## Metodologia
Para realizar a predição, iremos treinar um modelo de Machine Learning com os dados relacionados resultantes da análise realizada. A princípio, vamos tentar utilizar apenas um modelo simples de regressão, levando em consideração os erros relacionados ao modelo.

