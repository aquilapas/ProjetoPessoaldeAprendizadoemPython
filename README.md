# ProjetoPessoaldeAprendizadoemPython
Projeto Pessoal de Aprendizado em Python: Manipulação de Dados, Visualização, Integração com APIs e PLN
## 1. Descrição Detalhada

Este projeto tem como propósito consolidar o aprendizado em Python por meio do desenvolvimento de pequenos módulos que envolvem manipulação de dados, visualização, integração com APIs e aplicação prática de Processamento de Linguagem Natural (PLN). 

A proposta é usar bibliotecas amplamente adotadas no mercado e simular situações reais, documentando cada passo para reforço de conceitos e aplicação prática.

Os módulos do projeto foram organizados de forma sequencial, evoluindo em complexidade para garantir uma curva de aprendizado contínua e eficiente.

---

## 2. Objetivo

Aprimorar habilidades em Python por meio do estudo e aplicação prática de bibliotecas e técnicas essenciais, criando projetos que demonstrem o aprendizado, e gerar um portfólio público no GitHub com código limpo, funcional e documentado.

---

## 3. Métricas de Sucesso

### ✅ Manipulação de Dados com Pandas

**Importação de dados (até fev/25):**
- Leitura de arquivos nos formatos **CSV**, **Parquet**, **Avro** e **TXT** usando `pandas`.
- Conversão dos arquivos em **DataFrames padronizados** para análise.

**Filtragem e seleção (até mar/25):**
- Aplicação de **filtros condicionais** e seleções de colunas específicas.
- Salvamento de arquivos filtrados no formato **Parquet**.

**Transformações com Pandas (até abr/25):**
- Implementação de regras usando a lógica `np.where()` e `.apply()`, simulando **“CASE WHEN”** do SQL.

---

### ✅ Visualização de Dados

**Criação de 3 gráficos com Matplotlib (até mar/25):**
- **Gráfico de barras** comparando categorias.
- **Gráfico de linhas** com séries temporais.
- **Histograma** para distribuição de frequência.

---

### ✅ Integração com APIs

**5 chamadas a APIs REST (até mar/25):**
- Uso da biblioteca `requests` para chamadas **GET e POST**.
- **Tratamento de erros** com `try/except`.
- Extração de dados e **conversão para DataFrame**.
- Exemplo: consumo da API pública do IBGE, JSONPlaceholder, entre outras.

---

### ✅ Projeto Prático: Processamento de Linguagem Natural (PLN)

**Mini-projeto com base em dados reais (até abr/25):**
- Coleta de **tweets** ou **reviews**.
- **Tokenização** usando `nltk` ou `spaCy`.
- **Remoção de stopwords**.
- Aplicação de **análise de sentimento** com `TextBlob` ou `VADER`.
- Geração de **visualizações dos resultados** (palavras mais frequentes, polaridade, etc).

---

## Tópicos Desenvolvidos

### ✅ Manipulação de Dados com Pandas
- Leitura de arquivos: `.csv`, `.parquet`, `.txt`, `.avro`
- Filtros e seleções
- Transformações com `np.where` simulando `CASE WHEN`

### ✅ Visualização com Matplotlib
- Gráfico de barras
- Gráfico de linha
- Histograma

### ✅ Integração com APIs
- Requisições `GET` e `POST`
- Tratamento de respostas e erros
- Conversão em DataFrames

### ✅ Processamento de Linguagem Natural (PLN)
- Tokenização
- Remoção de stopwords
- Análise de sentimento com `TextBlob`

---

## Requisitos

- Python 3.8+
- Bibliotecas:
  - pandas
  - matplotlib
  - requests
  - textblob
  - nltk
  - fastavro
  - pyarrow

Instale com:

```bash
pip install pandas matplotlib requests textblob nltk fastavro pyarrow
