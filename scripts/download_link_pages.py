from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.safari.options import Options as SafariOptions
import time
import os

# Função para baixar o html de uma página
def download_link_pages(url, html_file_name):
    # configura opções do driver
    options = SafariOptions()
    options.add_argument('--headless=new') # Não funciona no Safari
    
    # abre o navegador Safari
    driver = webdriver.Safari(options=options)

    # navega para a página fornecida
    driver.get(url)

    # pega os cookies
    cookies = driver.get_cookies()
  
    # define o user agent
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    
    # espera 5 segundos
    #time.sleep(5)
 
    # especifica uma condição de espera
    try:
        wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'visaoQuadrosTd')))
    except Exception as e:
        print(f"Exceção lançada no arquivo: {html_file_name} : ",e)
    finally: 
        # salva o html em um arquivo
        with open(html_file_name, 'w', encoding='utf-8') as f:
            f.write(driver.page_source)
    
    driver.quit()