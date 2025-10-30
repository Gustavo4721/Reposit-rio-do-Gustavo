# Questão 1

import pandas as pd

file = 'cadastro_alunos.csv'
df = pd.read_csv(file)

df.head(5)
df.tail(5)

# Questão 2

df.shape[0]
df.shape[1]

# Questão 3

df.columns

# Questão 4

df.dtypes

# Questão 5

df.describe()

# Questão 6

df.info()

# Questão 7

file1 = 'imoveis_brasil.csv'
df = pd.read_csv(file1)

df['Tipo_Imovel'].unique()