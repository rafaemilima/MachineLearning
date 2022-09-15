# Atividade de Pré-Processamento de Dados

A presente atividade busca aplicar técnicas vistas em sala de aula a uma base de dados incompleta, para logo após submeter a mesma ao algoritmo KNN.
A descrição, bem como os arquivos base da atividade estão disponíveis no github: https://github.com/aydanomachado/mlclass/tree/master/01_Preprocessing

# Metodologia

Após diversos testes e diversas técnicas aplicadas, o método que nos garantiu uma acurácia de 63% será descrito abaixo, o mesmo está 
no arquivo preprocessing.py.

## Análise dos dados

Inicialmente buscamos obter o máximo de informações possíveis acerca dos dados, tentando assim estabelecer relações entre os mesmos. Para isso usamos métodos
da biblioteca pandas como o describe() e até mesmo ordenação para tentarmos obter alguma relação entre eles.

## Dropando as linhas com valores NaN

Após analisar a base, foram descobertos diversos valores faltando nas colunas dos atributos de Insulin e SkinThickness, bem como uma porcentagem menor, porém
ainda assim faltando nos atributos BMI, BloodPressure e Glucose.

Após diversos testes obtivemos bons resultados ao descartar todas as linhas de dados faltantes, garantindo assim que trabalhariamos (ainda que com menos dados),
com os dados reais coletados.

## Normalizando valores

Buscando aumentar nossa acurácia e deixar os valores da base na mesma escala, nós aplicamos a normalização Min-Max, deixando todos os valores em uma escala
entre 0 e 1.

## Drop de colunas

Após alguns testes atestamos que removendo algumas colunas nossa acurácia subia, portanto removemos as colunas Age e Pregnancies.

# Outras Metodologias

Inicialmente também tentamos alguns métodos que se provaram inferiores ou ineficazes ao listado acima, bem como carentes de certo refinamento, 
porém ainda assim interessantes para uma menção honrosa:

- Preencher os valores faltantes com constantes: Utilizamos aqui valores estatísticos (média, mediana), bem como valores aleatórios.
- Estabelecer relações entre os valores: Através desse método, estabelecemos uma relação entre a coluna de Glucose e Insulin para assim preencher a última
com valores mais próximos dos dados reais. No fim esse método serviu para estabelecer limites inferiores e superiores para gerar valores aleatórios nessa
coluna.

# Considerações Finais

Infelizmente no princípio seguimos um direcionamento que demandou bastante tempo e não gerou resultados tão interessantes, portanto não conseguimos aplicar
algumas das ideias que tinhamos em mente, como atribuir pesos diferentes para cada coluna ou remover mais colunas com uma correlação muito alta.

Entretanto acreditamos que apesar de pouco tempo para aplicar as técnicas mais mecânicas, conseguimos expandir nosso conhecimento na área e no uso das 
ferramentas, principalmente na biblioteca Pandas.
