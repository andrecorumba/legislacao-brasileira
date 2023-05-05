from download_link_pages import download_link_pages
import os

def link_pages_codigos():
    # Main para baixar as páginas com as os links para as leis por ano 
    folder = "/Volumes/DATA/data_legilacao_brasileira/link_pages"

    # Baixar a página com os links para as leis delegadas desde 1962
    url = "http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/codigos-1"
    print("Baixando Link Pages Códigos")
    download_link_pages(url,os.path.join(folder, "links_codigos.html") )
    print("Fim da execução!")

if __name__ == "__main__":
    link_pages_codigos()