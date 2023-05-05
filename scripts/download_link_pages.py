from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.safari.options import Options as SafariOptions
import time
import os


def find_link_pages(url, type_of_law, css_class_name, download_css_class_name):
    folder = "/Volumes/DATA/data_legilacao_brasileira/link_pages"
   
    # Abre o navegador Safari e passa parâmetros para acessar a página
    driver = webdriver.Safari()
    driver.get(url)
    cookies = driver.get_cookies()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    
    link_pages_list = []
    
    # Acessa a primeira página com os links para as leis
    try:
        wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, css_class_name)))
        link_pages_list = driver.find_elements(By.CLASS_NAME, css_class_name)
    except Exception as e:
        print(f"Exceção lançada: ",e)

    
    # Cria uma lista com os links das link pages
    url2_list = []
    for link_page in link_pages_list:
        url2_list.append(link_page.get_attribute("href"))
    
    # Fecha o driver para evitar conflitos
    driver.quit()    
    
    # Acessa cada link page e baixa o html daquela link page
    for url2 in url2_list:
        try: 
            html_file_name  = f"links_{type_of_law}_{url2.split('/')[-1]}.html"
            print("Baixando arquivo: ",html_file_name, "\n")
            download_link_pages(url2,os.path.join(folder, html_file_name), download_css_class_name )
        except Exception as e:
            print(f"Exceção lançada: ",e)
            continue

# Função para baixar o html de uma página
def download_link_pages(url, html_file_name, download_css_class_name):
    # configura opções do driver
    options = SafariOptions()
    #options.add_argument('--headless=new') # Modo headless não funciona no Safari
    
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
        wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, download_css_class_name)))
    except Exception as e:
        print(f"Exceção lançada no arquivo: {html_file_name} : ",e)
    finally: 
        # salva o html em um arquivo
        with open(html_file_name, 'w', encoding='utf-8') as f:
            f.write(driver.page_source)
    
    driver.quit()