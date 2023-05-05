# Este script acessa a pasta com os arquivos das link pages, 
# faz parser do html para buscar os links e baixa os arquivos.

import os
from bs4 import BeautifulSoup


from download_link_pages import download_link_pages

def download_laws():
    folder_link_pages = "/Volumes/DATA/data_legilacao_brasileira/link_pages"
    folder_destination = "/Volumes/DATA/data_legilacao_brasileira/html_legislacao"
    
    for file_name in os.listdir(folder_link_pages):
        if file_name.endswith(".html"):
            file_path = os.path.join(folder_link_pages, file_name)
            print(file_path)
            
            with open(file_path, "r") as f:
                html = f.read()
                soup = BeautifulSoup(html, "html.parser")
                download_css_class_name = [ "external-link", "visaoQuadrosTd"]
                links = soup.find_all("a", class_= download_css_class_name )

                # Cria uma lista com os links das link pages
                url_list = []
                for link in links:
                    url = link.get("href")

                    if url:
                        if url.startswith("http://www.planalto.gov.br/ccivil_03"):
                            print("Baixando url: \n", url)
                            try:
                                html_file_name = f"{url.split('/')[-1]}.html"
                                download_link_pages(url, os.path.join(folder_destination, html_file_name), download_css_class_name)
                            except Exception as e:
                                print(f"Exceção lançada:{url} ",e)
                                continue
                        else:
                            print("URL não baixada, pois não é do planalto:")
                            print(link)

                    else:
                        print("URL não encontrada")
                        print(link)

if __name__ == "__main__":
    download_laws()