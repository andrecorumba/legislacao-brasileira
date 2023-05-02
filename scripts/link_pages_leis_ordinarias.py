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

    html_file_name = f'links_leis_ordinarias_{year}.html'

    download_link_pages(url,os.path.join(folder, html_file_name) )

    print("Fim da execução!")


def link_pages_leis_ordinarias_anteriores():
    # Main para baixar as páginas com as os links para as leis por ano 
    folder = "/Volumes/DATA/data_legilacao_brasileira/link_pages"

    # Baixar a página com os decretos anterioes a 1960
    url_anteriores_a_1960 = "http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/leis-ordinarias/anteriores-a-1960-leis-ordinarias"
    print("Baixando Leis Ordinarias anteriores a 1960")
    download_link_pages(url_anteriores_a_1960,os.path.join(folder, "links_leis_ordinarias_anteriores_1960.html") )

    # Baixar a página com os decretos entre 1960 e 1969
    url_1960_a_1980 = "http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/leis-ordinarias/1980-a-1960-leis-ordinarias"
    print("Baixando Leis Ordinarias de 1960 a 1980")
    download_link_pages(url_1960_a_1980,os.path.join(folder, "links_leis_ordinarias_1960_a_1980.html") )

    # Baixar a página com os decretos entre 1970 e 1979
    url_1981_a_1987 = "http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/leis-ordinarias/1987-a-1981-leis-ordinarias"
    print("Baixando Leis Ordeianrias de 1981_a_1987")
    download_link_pages(url_1981_a_1987,os.path.join(folder, "links_leis_ordinarias_1981_a_1987.html") )

if __name__ == "__main__":
    link_pages_leis_ordinarias_anteriores()