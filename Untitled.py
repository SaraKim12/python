#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install pyautogui
#!pip install pyperclip


# In[2]:


import pyautogui
import pyperclip
import time

#passo1: entrar no sistema(entrar no link)

pyautogui.PAUSE = 1
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(5)

#passo2: navegar até o local do relatório(entrar na pasta exportar)

pyautogui.click(x=357, y=286, clicks = 2)
time.sleep(3)

#passo3: fazer o download do relatório
pyautogui.click(x=601, y=290)
pyautogui.click(x=1153, y=181)
pyautogui.click(x=936, y=595)
time.sleep(5)


# In[3]:


#passo4: Calcular os indicadores

import pandas as pd

tabela = pd.read_excel(r'C://Users/sukhe/Downloads/Vendas.Dez.xlsx')
display(tabela)
faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()


# In[4]:


#passo5: Entrar no email

pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://mail.google.com/mail/u/1/')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(5)

#passo6: Enviar por e-mail o resultado

pyautogui.click(x=93, y=212)

pyautogui.write('sukher2222@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
pyperclip.copy('Relatório de vendas')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')

texto = f"""
Prezados, bom dia

O faturamento de ontem foi de: {faturamento}
A quantidade de produtos foi de: {quantidade}
    
Abs
Sara Viana"""

pyperclip.copy(texto)
pyautogui.hotkey('ctrl','v')

pyautogui.hotkey('ctrl', 'enter')


# In[ ]:





# In[ ]:





# In[ ]:





# In[5]:


#time.sleep(5)
#pyautogui.position()


# In[ ]:




