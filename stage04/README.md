# Etapa 04 - Descrição da Proposta

## Motivação e Contexto
> Escolhemos o tema da gripe para o projeto, por ser um assunto bem relevante na área da saúde e que pode se relacionar bem com diversos fatores.
Assim é possível realizar uma proposta diversificada, além de facilitar a busca de dados de modelos variados.
O vírus da gripe muda todo ano, sendo necessário desenvolvimento de vacinas para acompanhar o combate a doença.
Assim, nossa motivação principal é a possibilidade de prever os casos de gripe esperados para determinado local e poder melhorar a profilaxia.

## Método
>Foram escolhidos algumas fontes de dados, que estão no tópico seguinte. 
Essas bases foram trabalhadas a fim de montar um banco de dados em SQL na etapa 3, e agora revisado na etapa 4.
Também foi trabalho uma parte para realizar análises com grafos, em Cypher.

>Iremos realizar algumas análises:
- predições relacionadas a gripe, como o número de casos esperados em determinado estado; 
- como esses casos estão distribuidos pelo país e como esse vírus se espalha geograficamente;

Por isso as bases de dados escolhidas estão relacionadas com o histórico de atuação desse vírus no Brasil, o que pode nos auxiliar a fazer predições, com a movimentação de pessoas pelo território nacional e como o histórico de temperatura do Brasil nos últimos anos, pois isso afeta diretamente como a gripe se espalha e também interfere na vida útil dos virús.
>As predições serão realizadas, utilizando Machine Learning, com os dados relacionados resultantes da análise, para isso utilizaremos um modelo simples de regressão, levando em consideração os erros relacionados ao modelo.
>Também serão exibidos algumas informações visuais com os dados do SGBD, a fim de exibir como o vírus se espalha geograficamente.

## Bases de Dados
> Bases de dados utilizadas no projeto:

título da base | link | breve descrição
----- | ----- | -----
`voos no brasil` | `https://www.anac.gov.br/assuntos/dados-e-estatisticas/historico-de-voos` | `datasets com voos no brasil, por ano e mês`
`infogripe` | `http://info.gripe.fiocruz.br` | `sistema de casos de gripe no brasil`
</br>

## Obtendo arquivos para gerar o SGBD
link do drive com todos os arquivos mencionados abaixo: </br>
https://drive.google.com/drive/folders/1G7e0yO-ugxZEp1H2t9dtGV_WrryjV_nH?usp=sharing </br>

### Fonte de dados de Voos no Brasil
Incialmente, baixamos as tabelas csv, no período de 2010 à 2019. Como as tabelas não seguiam o mesmo padrão, elas foram padronizadas individualmente,
apenas utilizando recursos do editor de texto. Desse modo, foram obtidos os arquivos csv base, para serem trabalhados e transformados em tabelas. Como o github 
não aceita arquivos muito grandes, tivemos de colocar no google drive. Os arquivos bases podem ser encontrados na pasta 01-BASE-VOOS. </br>

Em seguida, como eram muitas tabelas, 12 por ano, utilizamos um script para juntar as tabelas de mesmo ano. Não utilizamos o Jupyter/Binder para essa etapa, pois estavamos encontrando muitos problemas de execução, e dificuldade para abrir e processar as tabelas. Para não perder tempo resolvendo tais contratempos, e como os arquivos eram apenas intermediários, executamos diretamente na máquina. O script e os arquivos obtidos podem ser encontrados na pasta 02-PYTHON-VOOS-TOTAIS.</br>

Em seguida, esses dados foram trabalhados a primeira vez no Orange, a fim de facilitar o processo de separação dos dados. Com ele, obtemos os arquivos csv que podem 
ser encontrados na pasta 03-ORANGE-VOOS (os arquivos do orange também estão nessa pasta).

### Fonte de casos de Gripe no Brasil
Para estes dados, seria necessário baixar centenas de csvs pelo sistema do infogripe, pois o sistema não tem uma api de acesso direta aos dados.
Entretanto, encontramos um projeto de um grupo que já fez essa parte de juntar os dados de cada semana, para todos os anos e estados. Assim, utilizamos
o csv do repositório deles, que pode ser encontrado no link a seguir:</br>
https://github.com/belisards/srag_brasil </br> 
ou na pasta  - BASE CASOS. </br>

O arquivo que utilizamos foi o casos_uf.csv. Em seguida, esse arquivo foi preparado no Orange, a fim de tirar as colunas desnecessárias e remover os dados de 2009.
Como resultado, obtivemos o arquivo casos01.csv. O arquivo do orange e o csv, podem ser encontrados na pasta 2 - ORANGE CASOS.

## Obtendo o SGBD
### Criando Tabelas 
Foram geradas 5 tabelas até o momento: </br>
- Estado </br>
- Cidade </br>
- Aeroporto </br>
- Voo </br>
- Casos </br>

A query de criação das tabelas que vieram dos arquivos de voos, estão na raiz da pasta VOOS. Dessas tabelas, a tabela estado é a única que teve os inserts criados
do zero, e a query para isso também se encontra na raiz. Os dados de inserção para as outras tabelas podem ser encontrados na pasta 04 - GERAÇÃO DE QUERIES DE INSERT.

A query de criação da tabela de casos está na raiz da pasta CASOS. Os inserts dessa tabela foram gerados com um script python, tal que ambos podem ser encontrados
na pasta 3 - GERAÇÃO DE QUERIES DE INSERT.

### Entidade Relacionamento
O modelo entidade relacionamento foi criado com base na junção das fontes de dados trabalhadas até o momento, e o diagrama pode ser encontrado na raiz da pasta stage03.

### Outras Queries
Algumas queries que podem ser utilizadas para análise futura, foram criadas e colocadas na raiz da pasta stage03.

## Considerações futuras
Não conseguimos inserir a tabela de clima a tempo, como encontramos uma quantidade de dados considerável para 
os dados de casos e de voos, achamos melhor buscar uma fonte com dados de clima que seja mais completa. Entretanto,
como ainda não encontramos uma fonte que possua estes dados, deixamos para implementar na próxima etapa. Se não 
obtivermos sucesso, tentaremos buscar outras fontes de dados que possam ser integradas. Outra coisa que deve ser feita no futuro,
é padronizar o uso das datas, já que os casos estão classificados por semana, e os voos no formato de data padrão. 

Em relação ao processo de transformar as fontes em um sgbd, achamos muito complicado juntar os dados todos, bem 
como encontrar as fontes de maneira que poderiamos utilizar. Também tivemos limitações com o uso do github, pelo tamanho dos arquivos,
e com o uso de notebook. Entretanto, as queries foram geradas como desejado, apesar das dificuldades.
