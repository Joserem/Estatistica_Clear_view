import pandas as pd
import numpy as np
import random

# Criando um DataFrame com dados fictícios
df = pd.DataFrame({
    'Data': pd.date_range(start='1/1/2023', periods=100),
    'Vendas': np.random.randint(100, 1000, size=100),
    'Despesas': np.random.randint(50, 500, size=100),
    'Satisfacao': np.random.randint(1, 10, size=100)
})

# Lista de categorias de produtos fictícios
categorias_produtos = ['Eletrônicos', 'Roupas', 'Alimentos', 'Livros', 'Móveis', 'Jogos', 'Esportes', 'Jardinagem']

# Adicionando a coluna 'Produtos' ao DataFrame
df['Produtos'] = [random.choice(categorias_produtos) for _ in range(len(df))]

# Salvando o DataFrame atualizado como um arquivo Excel
df.to_excel('dados_empresa.xlsx', index=False)
