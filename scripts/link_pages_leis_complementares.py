from download_link_pages import download_link_pages
import os

def link_pages_leis_complementares():
    ''' Função para baixar as páginas com os links para as leis complementares.
        Todas os links para essas leis estão em uma única página.
    '''

    folder = "/Volumes/DATA/data_legilacao_brasileira/link_pages"

    print("Baixando página de inks das Leis complementares")

    url = 'http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/leis-complementares-1/todas-as-leis-complementares-1'

    html_file_name = f'links_leis_complementares_ate_abril_2023.html'

    download_link_pages(url,os.path.join(folder, html_file_name) )

    print("Fim da execução!")

if __name__ == "__main__":
    link_pages_leis_complementares()