import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

chrome = webdriver.Chrome(options=chrome_options)
chrome.maximize_window()
chrome.get('https://dlp.hashtagtreinamentos.com/python/intensivao/login')

email_input = chrome.find_element(By.ID, 'email')
email_input.clear()
email_input.send_keys('kaique.github@gmail.com')
email_input.send_keys(Keys.RETURN)

password_input = chrome.find_element(By.ID, 'password')
password_input.clear()
password_input.send_keys('Jesus')
password_input.send_keys(Keys.RETURN)

login_button = chrome.find_element(By.ID, 'pgtpy-botao')
login_button.click()

produtos = pd.read_csv('products_automation/produtos.csv')

for count in range(len(produtos)):

    codigo_input = chrome.find_element(By.ID, 'codigo')
    codigo_input.clear()
    codigo_input.send_keys(produtos['codigo'][count])
    codigo_input.send_keys(Keys.RETURN)

    marca_input = chrome.find_element(By.ID, 'marca')
    marca_input.clear()
    marca_input.send_keys(produtos['marca'][count])
    marca_input.send_keys(Keys.RETURN)

    tipo_input = chrome.find_element(By.ID, 'tipo')
    tipo_input.clear()
    tipo_input.send_keys(produtos['tipo'][count])
    tipo_input.send_keys(Keys.RETURN)

    categoria_input = chrome.find_element(By.ID, 'categoria')
    categoria_input.clear()
    categoria_input.send_keys(str(produtos['categoria'][count]))
    categoria_input.send_keys(Keys.RETURN)

    preco_input = chrome.find_element(By.ID, 'preco_unitario')
    preco_input.clear()
    preco_input.send_keys(str(produtos['preco_unitario'][count]))
    preco_input.send_keys(Keys.RETURN)

    custo_input = chrome.find_element(By.ID, 'custo')
    custo_input.clear()
    custo_input.send_keys(str(produtos['custo'][count]))
    custo_input.send_keys(Keys.RETURN)

    observacao_input = chrome.find_element(By.ID, 'obs')
    observacao_input.clear()
    observacao_input.send_keys(produtos['obs'][count])
    observacao_input.send_keys(Keys.RETURN)




