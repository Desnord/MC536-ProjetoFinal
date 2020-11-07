# Etapa 03 - Descrição da Proposta

## Motivação e Contexto
> Escolhemos o tema da gripe para o projeto, por ser um assunto bem relevante na área da saúde e que pode se relacionar bem com diversos fatores.
Assim é possível realizar uma proposta diversificada, além de facilitar a busca de dados de modelos variados.
O vírus da gripe muda todo ano, sendo necessário desenvolvimento de vacinas para acompanhar o combate a doença.
Assim, nossa motivação principal é a possibilidade de prever os casos de gripe esperados para determinado local e poder melhorar a profilaxia.

## Método
>Foram escolhidos algumas fontes de dados, que estão no tópico seguinte. Essas bases foram trabalhadas a fim de montar um banco de dados em SQL.
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

### Fonte de dados de Voos no Brasil
Incialmente, baixamos as tabelas csv, no período de 2010 à 2019. Como as tabelas não seguiam o mesmo padrão, elas foram padronizadas individualmente,
apenas utilizando recursos do editor de texto. Desse modo, foram obtidos os arquivos csv base, para serem trabalhados e transformados em tabelas. Como o github 
não aceita arquivos muito grandes, estes arquivos podem ser encontrados no drive a seguir:</br>
https://drive.google.com/drive/folders/1_iJDpGbzD3YcEj_K5Iffd7mADJ_9193I?usp=sharing</br>

Inicialmente, como eram muitas tabelas, 12 por ano, utilizamos um script para juntar as tabelas de mesmo ano. Não utilizamos o Jupyter/Binder para essa etapa, pois estavamos encontrando muitos problemas de execução, e dificuldade para abrir e processar as tabelas. Para não perder tempo resolvendo tais contratempos, e como os arquivos eram apenas intermediários, executamos diretamente na máquina. Os arquivos obtidos podem ser encontrados à seguir:</br>
https://drive.google.com/drive/folders/1lkjfuRiZ9Ll7kzrC311Hh_MCL_bJJ5sP?usp=sharing</br>

O script dessa parte pode ser encontrado na pasta f3, com o nome de voosTotais.py </br>

Em seguida, esses dados foram trabalhados a primeira vez no Orange, a fim de facilitar o processo de separação dos dados. Com ele, obtemos os arquivos csv que podem 
ser encontrados no endereço a seguir (estes csvs que serão utilizados para criar as tabelas de Cidade, Voo e Aeroporto):</br>
https://drive.google.com/drive/folders/1mDot2bxqHiSGIHXnkX2PU5qSwm4ZT8p1?usp=sharing</br>

E os arquivos do orange:</br>
https://drive.google.com/drive/folders/1BE1LcNpOIQGIuQQx1pj6wcWrxM1u00sS?usp=sharing</br>

### Fonte de dados Climáticos no Brasil

### Fonte de casos de Gripe no Brasil

## f1 - primeiro modelo conceitual do projeto
https://github.com/Desnord/ProjetoFinalMC536/tree/main/stage03/f1 </br>
Imagem com o primeiro diagrama Entidade Relacionamento do projeto.

## f2 - modelos lógicos dos bancos de dados relacionados aos modelos conceituais
https://github.com/Desnord/ProjetoFinalMC536/tree/main/stage03/f2 </br>
Imagem de esquema do modelo lógico, relacionado ao modelo conceitual, e a query de criação das tabelas.

## f3 - primeiro programa de extração e conversão de dados no Jupyter Notebook via Binder
https://github.com/Desnord/ProjetoFinalMC536/tree/main/stage03/f3 </br>
Notebook contendo os códigos em Python, utilizados para gerar as queries.

## f4 - primeiro conjunto de queries no Jupyter Notebook via Binder
https://github.com/Desnord/ProjetoFinalMC536/tree/main/stage03/f4 </br>
Notebook contendo as queries SQL.

## f5 - arquivos relacionais (usalmente CSV), XML ou JSON que não estejam disponíveis online e sejam acessados pelo notebook
https://github.com/Desnord/ProjetoFinalMC536/tree/main/stage03/f5 </br>
Arquivos csv utilizados para criação do SGBD.

## f6 - arquivos extras
https://github.com/Desnord/ProjetoFinalMC536/tree/main/stage03/f6 </br>
Arquivos que não se encaixam em nenhuma das opções acima, e que foram utilizados no projeto.
