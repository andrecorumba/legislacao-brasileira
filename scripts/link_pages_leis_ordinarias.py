from download_link_pages import download_link_pages
import os


def main():
    # Main para baixar as páginas com as os links para as leis por ano 
    #folder = "/Volumes/DATA/data_legilacao_brasileira/link_pages"
    folder = "data"

    # Fazer um for de 1988 até 2023 para baixar todas as páginas
    for year in range(1988,2023):
    
        print("Baixando ano: ", year)
    
        url = f'http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/leis-ordinarias/{year}-leis-ordinarias'
    
        html_file_name = f'links_leis_ordinarias_{year}.html'
    
        download_link_pages(url,os.path.join(folder, html_file_name) )

    print("Fim da execução!")

def only_one_year():
    # Main para baixar as páginas com as os links para as leis por ano 
    folder = "data"

    year = '2023'
    
    print("Baixando ano: ", year)

    url = f'http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/leis-ordinarias/{year}-leis-ordinarias'

    # url do ano de 1997 e 2011 são diferentes
    #url = 'http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/leis-ordinarias/1997-leis-ordinarias-1'
    #url = 'http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/leis-ordinarias/2011-leis-ordinarias-1'

    html_file_name = f'links_leis_ordinarias_{year}_phantom.html'

    download_link_pages(url,os.path.join(folder, html_file_name) )

    print("Fim da execução!")


if __name__ == "__main__":
    #main()
    only_one_year()