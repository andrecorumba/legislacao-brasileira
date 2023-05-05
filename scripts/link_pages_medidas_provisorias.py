from download_link_pages import download_link_pages, find_link_pages
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.safari.options import Options as SafariOptions
    

if __name__ == "__main__":
    #link_pages_medidas_provisorias()
    url = "http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/medidas-provisorias"
    type_of_law = "medidas_provisorias"
    css_class_name = "internal-link"
    download_css_class_name = "visaoQuadrosTd"

    find_link_pages(url, type_of_law, css_class_name, download_css_class_name)