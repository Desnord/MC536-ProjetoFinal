# Etapa 03 - Descrição da Proposta

## Motivação e Contexto
> Escolhemos o tema da gripe para o projeto, por ser um assunto bem relevante na área da saúde e que pode se relacionar bem com diversos fatores.
Assim é possível realizar uma proposta diversificada, além de facilitar a busca de dados de modelos variados.
O vírus da gripe muda todo ano, sendo necessário desenvolvimento de vacinas para acompanhar o combate a doença.
Assim, nossa motivação principal é a possibilidade de prever os casos de gripe esperados para determinado local e poder melhorar a profilaxia.

## Método
>As principais análises que serão feitas, envolvem predições relacionadas a gripe, como o número de casos esperados em determinada cidade, como esses casos estão distribuidos pelo país e como esse vírus se espalha geograficamente, por isso as bases de dados escolhidas estão relacionadas com o histórico de atuação desse vírus no Brasil, o que pode nos auxiliar a fazer predições, com a movimentação de pessoas pelo território nacional e como o histórico de temperatura do Brasil nos últimos anos, pois isso afeta diretamente como a gripe se espalha e também interfere na vida útil dos virús.
>As predições serão realizadas, utilizando Machine Learning, com os dados relacionados resultantes da análise, para isso utilizaremos um modelo simples de regressão, levando em consideração os erros relacionados ao modelo.
>Também serão exibidos algumas informações visuais com os dados do SGBD.

## Bases de Dados
> Bases de dados utilizadas no projeto:

título da base | link | breve descrição
----- | ----- | -----
`voos no brazil` | `https://www.kaggle.com/ramirobentes/flights-in-brazil` | `dataset com todos os voos que do espaço aéreo brasileiro de alguns anos`


# f1 - primeiro modelo conceitual do projeto;
Imagem com o primeiro diagrama Entidade Relacionamento do projeto.

# f2 - modelos lógicos dos bancos de dados relacionados aos modelos conceituais;
Imagem dos modelo lógico, obtido a partir do modelo conceitual.

# f3 - primeiro programa de extração e conversão de dados no Jupyter Notebook via Binder;
Notebook contendo os códigos em Python, utilizados para gerar as queries

# f4 - primeiro conjunto de queries no Jupyter Notebook via Binder;
Notebook contendo as queries SQL.

# f5 - arquivos relacionais (usalmente CSV), XML ou JSON que não estejam disponíveis online e sejam acessados pelo notebook;
Arquivos csv utilizados para criação do SGBD.

# f6 - arquivos extras;
Arquivos que não se encaixam em nenhuma das opções acima, e que foram utilizados no projeto.

# --
# --
# --
# --
# Visão Geral
O objetivo geral do projeto final desta disciplina é realizar a análise de dados relacionados à saúde, para usá-los
em uma das seguintes possíveis tarefas: recomendação, estudo de associações, validação de hipóteses, análise
exploratória, análise visual, análise comparativa e predição.
A análise envolverá dados de, pelo menos, três fontes na Web cada uma com um modelo lógico diferente.

# Etapa 3
Nesta etapa serão solicitadas duas entregas: modelagem inicial e primeiro conjunto de análises em um dos
modelos lógicos.

Deve ser detalhada a primeira versão dos modelos (conceitual e lógico) que a equipe usará para a análise.
Trata-se um modelo preliminar, que poderá ser modificado no futuro, serve para a equipe mostrar o ponto de partida
para as análises pretendidas. O modelo é uma combinação de uma “engenharia reversa” dos modelos das bases de
origem (selecionando apenas os dados utilizados na análise), mais atributos/tabelas/associações que vão ser
produzidos pelas equipes com vistas na análise. Por exemplo, a equipe pode decidir criar uma associação (que não
existia) entre duas fontes de dados distintas.

Por ser um modelo preliminar, a equipe poderá modificá-lo posteriormente.

Também deve ser escolhido um dos modelos lógicos para a entrega de uma primeira versão de análises. A
equipe pode escolher qualquer um dos modelos (tabelas, hierárquico ou rede), mas sugere-se o modelo relacional
(tabelas), pois foi o tratado com mais detalhes em sala. Devem ser observados aspectos de normalização no modelo
lógico.

Para o modelo escolhido, deve ser apresentado um primeiro programa de conversão de dados e um primeiro
conjunto de análises usando recursos de bancos de dados. Entende-se por recursos de bancos de dados o código
envolvendo um SGBD, ou seja, não deve ser feito processamento completamente em memória. Se for escolhido
modelo tabular, a sugestão é o uso de SQL.

Por ser um primeiro conjunto de análises, ele poderá ser refinado e expandido posteriormente. Uma sugestão é
um conjunto de, pelo menos, cinco queries de complexidade média em SQL que apresente resultados interessantes de
análise.

# Entrega
Deve ser disponibilizada no Github da equipe, conforme template disponibilizado em: 
https://github.com/santanche/lab2learn/blob/master/templates/project.md. É importante ressaltar que o documento da Fase 3 deve incluir os campos da Fase 2 (revisados, se necessário). Além disso, deverá constar:
- primeiro modelo conceitual do projeto
- modelos lógicos dos bancos de dados relacionados aos modelos conceituais;
- primeiro programa de extração e conversão de dados no Jupyter Notebook via Binder;
- primeiro conjunto de queries no Jupyter Notebook via Binder;
- arquivos relacionais (usalmente CSV), XML ou JSON que não estejam disponíveis online e sejam acessados pelo notebook.

Se não for possível executar no Jupyter/Binder a equipe deve apresentar justificativa pertinente.
