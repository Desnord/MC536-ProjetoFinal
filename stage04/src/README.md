# Instruções

## Gerar CSVs
Os arquivos .py foram utilizados para gerar os CSV finais e os arquivos SQL nesta pasta.
Para executar cada script, está comentado os csvs necessários como entrada. Além disso, é necessário
algumas bibliotecas para executar o código, como o pandas. 

## visualgraphs.html
Como é um arquivo html, basta baixa e executar no navegador.
Entretanto, o neo4j que está configurado, já foi apagado (ele é apagado depois de poucos dias pelo site) e não aparecerá nada na tela.
Para que o grafo apareça, é necessário criar um novo sandbox no neo4j e executar os comandos do cypher apresentados no stage04. Após isso,
na tela inicial do neo4j encontramos as informações para acessar o banco de dados, clicando para ver as informações do projeto e depois em "connection details".
Com as informações dessa aba, é só alterar os seguintes campos do documento html:

server_url: "sua Bolt URL"
server_user: "neo4j"
server_password: "sua password"
