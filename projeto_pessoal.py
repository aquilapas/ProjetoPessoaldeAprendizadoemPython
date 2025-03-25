# Projeto Pessoal de Aprendizado em Python

## manipulacao_dados/leitura_csv_parquet_avro_txt.py

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import fastavro

# Leitura de CSV
df_csv = pd.read_csv('dados/exemplo.csv')

# Leitura de Parquet
df_parquet = pd.read_parquet('dados/exemplo.parquet')

# Leitura de TXT delimitado por tabulacao
df_txt = pd.read_csv('dados/exemplo.txt', delimiter='\t')

# Leitura de Avro
with open('dados/exemplo.avro', 'rb') as f:
    reader = fastavro.reader(f)
    df_avro = pd.DataFrame([r for r in reader])

print(df_csv.head())
print(df_parquet.head())
print(df_txt.head())
print(df_avro.head())


## manipulacao_dados/filtros_transformacoes_case_when.py

import pandas as pd
import numpy as np

# Exemplo com DataFrame fictício
df = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'idade': [22, 35, 17, 45]
})

# Filtro: maiores de idade
maiores_idade = df[df['idade'] >= 18]

# Transformação: Classificação por faixa etária
df['faixa_etaria'] = np.where(df['idade'] < 18, 'menor',
                        np.where(df['idade'] <= 40, 'adulto jovem', 'meia idade'))

# Salvando como parquet
maiores_idade.to_parquet('dados/maiores_idade.parquet')

print(df)


## visualizacao_dados/graficos_matplotlib.py

import pandas as pd
import matplotlib.pyplot as plt

# Dataset exemplo
df = pd.DataFrame({
    'categoria': ['A', 'B', 'C'],
    'valor': [10, 20, 15],
    'tempo': pd.date_range(start='2024-01-01', periods=3)
})

# Gráfico de barras
plt.figure()
df.plot(kind='bar', x='categoria', y='valor', title='Gráfico de Barras')
plt.savefig('graficos/barra.png')

# Gráfico de linhas
plt.figure()
df.plot(kind='line', x='tempo', y='valor', title='Gráfico de Linha')
plt.savefig('graficos/linha.png')

# Histograma
plt.figure()
df['valor'].plot(kind='hist', title='Histograma')
plt.savefig('graficos/histograma.png')


## integracao_apis/chamadas_api_requests.py

import requests
import pandas as pd

# GET simples
res = requests.get('https://jsonplaceholder.typicode.com/posts')
posts = res.json()
df_posts = pd.DataFrame(posts)

# POST simulando envio de dados
payload = {'title': 'teste', 'body': 'conteudo', 'userId': 1}
res_post = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)
print(res_post.status_code, res_post.json())

# GET com tratamento de erro
try:
    res = requests.get('https://jsonplaceholder.typicode.com/users')
    res.raise_for_status()
    df_users = pd.DataFrame(res.json())
except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")

print(df_users.head())


## projeto_pln/analise_sentimento.py

import pandas as pd
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')
nltk.download('stopwords')

# Dados de exemplo
df = pd.DataFrame({
    'texto': [
        'Eu amo aprender Python!',
        'Esse curso é muito ruim.',
        'O conteúdo está bem explicado.'
    ]
})

# Tokenização e remoção de stopwords
stop_words = set(stopwords.words('portuguese'))

def limpar_texto(texto):
    tokens = word_tokenize(texto.lower())
    return ' '.join([t for t in tokens if t.isalpha() and t not in stop_words])

df['texto_limpo'] = df['texto'].apply(limpar_texto)

# Análise de sentimento
df['sentimento'] = df['texto_limpo'].apply(lambda x: TextBlob(x).sentiment.polarity)

print(df)
