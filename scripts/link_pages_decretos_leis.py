from download_link_pages import download_link_pages
import os

def link_pages_decretos_leis():
    # Main para baixar as páginas com as os links para as leis por ano 
    folder = "/Volumes/DATA/data_legilacao_brasileira/link_pages"

    # Baixar a link page dos decretos leis de 1937 a 1946
    url_1937_a_1946 = "http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/decretos-leis/1937-a-1946-decretos-leis-1"
    print("Baixando Link Pages Decretos Leis 1937_a_1946")
    download_link_pages(url_1937_a_1946,os.path.join(folder, "links_decretos_leis_1937_a_1946.html") )
    print("Fim da execução!")

    # Baixar a link page dos decretos leis de 1937 a 1946
    url_1965_a_1988 = "http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/decretos-leis/1965-a-1988-decretos-leis"
    print("Baixando Link Pages Decretos Leis 1965_a_1988")
    download_link_pages(url_1965_a_1988,os.path.join(folder, "links_decretos_leis_1965_a_1988.html") )
    print("Fim da execução!")

if __name__ == "__main__":
    link_pages_decretos_leis()