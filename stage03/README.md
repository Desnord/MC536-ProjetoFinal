# Etapa 03 - Descrição da Proposta

## Motivação e Contexto
> Escolhemos o tema da gripe para o projeto, por ser um assunto bem relevante na área da saúde e que pode se relacionar bem com diversos fatores.
Assim é possível realizar uma proposta diversificada, além de facilitar a busca de dados de modelos variados.
O vírus da gripe muda todo ano, sendo necessário desenvolvimento de vacinas para acompanhar o combate a doença.
Assim, nossa motivação principal é a possibilidade de prever os casos de gripe esperados para determinado local e poder melhorar a profilaxia.

## Método
>Foram escolhidos algumas fontes de dados, que estão no tópico seguinte. Essas bases foram trabalhadas a fim de montar um banco de dados em SQL.

### Para a fonte dos voos no Brasil, baixamos o csv e atráves do Orange, foram obtidos dois arquivos csv:
- cidade.csv </br>
Esse arquivo trás uma lista com tuplas de cidades, com seu nome, estado, longitude e latitude. Porém há cidades repetidas.
Através de um script em python, removemos as cidades repetidas e geramos um arquivo sql com os comandos de inserção. 

- voo.csv </br>
Esse arquivo trás uma lista com tuplas de voos realizados, com nome da cidade de origem, nome da cidade de destino, data de partida e data de chegada.
Novamente, com um script em python, geramos um arquivo sql com os comandos de inserção. 

>As principais análises que serão feitas, envolvem predições relacionadas a gripe, como o número de casos esperados em determinada cidade, como esses casos estão distribuidos pelo país e como esse vírus se espalha geograficamente, por isso as bases de dados escolhidas estão relacionadas com o histórico de atuação desse vírus no Brasil, o que pode nos auxiliar a fazer predições, com a movimentação de pessoas pelo território nacional e como o histórico de temperatura do Brasil nos últimos anos, pois isso afeta diretamente como a gripe se espalha e também interfere na vida útil dos virús.
>As predições serão realizadas, utilizando Machine Learning, com os dados relacionados resultantes da análise, para isso utilizaremos um modelo simples de regressão, levando em consideração os erros relacionados ao modelo.
>Também serão exibidos algumas informações visuais com os dados do SGBD.

## Bases de Dados
> Bases de dados utilizadas no projeto:

título da base | link | breve descrição
----- | ----- | -----
`voos no brazil` | `https://www.kaggle.com/ramirobentes/flights-in-brazil` | `dataset com todos os voos que do espaço aéreo brasileiro de alguns anos`


## f1 - primeiro modelo conceitual do projeto
https://github.com/Desnord/ProjetoFinalMC536/tree/main/stage03/f1 </br>
Imagem com o primeiro diagrama Entidade Relacionamento do projeto.

## f2 - modelos lógicos dos bancos de dados relacionados aos modelos conceituais
https://github.com/Desnord/ProjetoFinalMC536/tree/main/stage03/f2 </br>
Imagem dos modelo lógico, obtido a partir do modelo conceitual.

## f3 - primeiro programa de extração e conversão de dados no Jupyter Notebook via Binder
https://github.com/Desnord/ProjetoFinalMC536/tree/main/stage03/f3 </br>
Notebook contendo os códigos em Python, utilizados para gerar as queries

## f4 - primeiro conjunto de queries no Jupyter Notebook via Binder
https://github.com/Desnord/ProjetoFinalMC536/tree/main/stage03/f4 </br>
Notebook contendo as queries SQL.

## f5 - arquivos relacionais (usalmente CSV), XML ou JSON que não estejam disponíveis online e sejam acessados pelo notebook
https://github.com/Desnord/ProjetoFinalMC536/tree/main/stage03/f5 </br>
Arquivos csv utilizados para criação do SGBD.

## f6 - arquivos extras
https://github.com/Desnord/ProjetoFinalMC536/tree/main/stage03/f6 </br>
Arquivos que não se encaixam em nenhuma das opções acima, e que foram utilizados no projeto.
