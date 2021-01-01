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
