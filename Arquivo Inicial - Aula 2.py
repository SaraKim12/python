#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python
# 
# ### Desafio:
# 
# Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.
# 
# O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.
# 
# Isso representa uma perda de milhões para a empresa.
# 
# O que a empresa precisa fazer para resolver isso?
# 
# Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing <br>
# Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset

# In[3]:


#passo1: importar a base de dados

import pandas as pd

tabela = pd.read_csv('telecom_users.csv')

#passo2: visualizar a base de dados

tabela = tabela.drop('Unnamed: 0', axis = 1)
display(tabela)

#        entender quais informações tão disponíveis
#        descobrir as cagadas da base de dados


# In[4]:


#passo3: tratamento de dados
#        valores que estão reconhecidos de forma errada

tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors = 'coerce')

#        valores vazios
#        deletar as colunas vazias

tabela = tabela.dropna(how = 'all', axis = 1)

#        deletar linhas vazias

tabela = tabela.dropna(how = 'any', axis = 0)


display(tabela.info())


# In[5]:


#passo4: análise inicial

print(tabela['Churn'].value_counts())
print(tabela['Churn'].value_counts(normalize = True))


# In[11]:


#passo5: análise mais completa
#comparar cada coluna da minha tabela com a coluna de cancelamento

import plotly.express as px

#criar o gráfico

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x = coluna, color = 'Churn')

    grafico.show()


# In[7]:


#!pip install plotly


# ### Conclusões e Ações

# Escreva aqui suas conclusões:
# 
# - Cliente com contrato mensal tem muito mais chance de cancelar:
#      .podemos fazer promoções para o cliente ir para o contrato anual
#      
# 
