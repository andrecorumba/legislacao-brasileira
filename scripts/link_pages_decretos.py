from download_link_pages import download_link_pages
import os

def decretos_faltantes():
    # Baixa os decretos que derram erro na primeira execução.
    folder = "/Volumes/DATA/data_legilacao_brasileira/link_pages"
    faltantes  = [1989, 1991, 1992, 1995, 1996, 1997, 1999, 2001, 2007, 2008, 2009, 2012, 2016, 2018, 2019, 2020, 2021, 2022, 2023]
    #faltantes  = [2012]
    
    for year in faltantes:
        print("Baixando ano: ", year)
        url = f"http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/decretos1/{year}-decretos"
        #url = f"http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/decretos1/2012-decretos-2" # url de 2012
        html_file_name = f'links_decretos_{year}.html'
        download_link_pages(url,os.path.join(folder, html_file_name) )


def link_pages_decretos():
    # Main para baixar as páginas com as os links para as leis por ano 
    folder = "/Volumes/DATA/data_legilacao_brasileira/link_pages"

    # Baixar a página com os decretos anterioes a 1960
    url_anteriores_a_1960 = "http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/decretos1/anteriores-a-1960-decretos"
    print("Baixando Decretos anteriores a 1960")
    download_link_pages(url_anteriores_a_1960,os.path.join(folder, "links_decretos_anteriores_1960.html") )

    # Baixar a página com os decretos entre 1960 e 1969
    url_1960_a_1969 = "http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/decretos1/1969-a-1960-decretos-1"
    print("Baixando Decretos de 1960 a 1969")
    download_link_pages(url_1960_a_1969,os.path.join(folder, "links_decretos_1960_a_1969.html") )

    # Baixar a página com os decretos entre 1970 e 1979
    url_1970_a_1979 = "http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/decretos1/1979-a-1970-decretos-1"
    print("Baixando Decretos de 1970 a 1979")
    download_link_pages(url_1970_a_1979,os.path.join(folder, "links_decretos_1970_a_1979.html") )


    # Baixar os decretos de 1980 a 2023 (02/05/2023)
    for year in range(1980,2023):
    
        print("Baixando ano: ", year)
    
        url = f'http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/decretos1/{year}-decretos-1'
    
        html_file_name = f'links_decretos_{year}.html'
    
        download_link_pages(url,os.path.join(folder, html_file_name) )

    print("Fim da execução!")

if __name__ == "__main__":
    #link_pages_decretos()
    decretos_faltantes()