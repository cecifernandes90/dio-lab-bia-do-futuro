# Base de Conhecimento

## Visão Geral
O agente utiliza dados estruturados para apoiar o planejamento financeiro do usuário, com foco na construção de um escritório em casa. A base de conhecimento é composta por arquivos locais em formato CSV.

## Fontes de Dados Utilizadas

### 1. transacoes.csv
Contém o histórico financeiro do usuário, incluindo receitas e despesas.

**Principais campos esperados:**
- data
- tipo (receita/despesa)
- valor
- categoria
- descricao

## Estratégia de Uso dos Dados

O agente utiliza o arquivo `transacoes.csv` para:

- Analisar padrões de gastos do usuário
- Identificar possíveis economias mensais
- Calcular quanto o usuário pode destinar para atingir sua meta
- Apoiar a criação de um plano financeiro para montagem do escritório

## Adaptações Realizadas

Foi introduzido o conceito de **meta financeira**, que representa o valor necessário para construir o escritório em casa.

Essa meta pode ser:
- Informada diretamente pelo usuário
- Ou estimada com base em categorias relevantes (ex: móveis, equipamentos, iluminação)

## Acesso aos Dados

Os dados são carregados localmente pela aplicação em Python, utilizando bibliotecas como `pandas` para leitura do CSV.

Exemplo de carregamento:
```python
import pandas as pd

df = pd.read_csv("data/transacoes.csv")