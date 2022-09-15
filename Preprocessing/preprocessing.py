"""
Atividade de pré-processamento dos dados.

Criação de modelo preditivo para diabetes e envio para verificação de peformance
no servidor.

Equipe: Backend Boys
Integrantes: Rick Martim Lino dos Santos e Rafael Emílio Lima Alves
"""

import pandas as pd
from sklearn import preprocessing

# Fazendo a leitura do arquivo CSV diretamente do repositório
df = pd.read_csv('https://raw.githubusercontent.com/aydanomachado/mlclass/master/01_Preprocessing/diabetes_dataset.csv')

print(df.describe())  # Obtendo uma descrição dos dados para análise

# Removendo linhas com valores nulos nas colunas Glucose, BloodPressure, BMI e Insulin
df = df[df['Glucose'].notna()]
df = df[df['BloodPressure'].notna()]
df = df[df['BMI'].notna()]
df = df[df['Insulin'].notna()]

# Removendo colunas Age e Pregnancies
df.drop('Age', inplace=True, axis=1)
df.drop('Pregnancies', inplace=True, axis=1)

# Normalizando dados usando o escalador MinMax
columns = df.columns  # obtendo o header das colunas do csv
scaler = preprocessing.MinMaxScaler()
d2 = scaler.fit_transform(df)
scaled_df2 = pd.DataFrame(d2, columns=columns)

print(scaled_df2.head())  # printando as cinco primeiras linhas do csv
print(scaled_df2.describe())  # printando o describe para análise dos dados ao fim do pré-processamento


scaled_df2.to_csv('diabetes_dataset.csv', index=False)

