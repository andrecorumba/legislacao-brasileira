import os
import bs4

# Ler pasta com link pages. Return list_link_pages
def read_folder_link_pages(folder):
    file_list= [os.path.join(folder,file) for file in os.listdir(folder)]
    return file_list
    
# To Do Fazer Parser html.
def parser_link_pages(file_list):
    '''
    Baixar as urls das páginas de leis e decretos. 
    O link está na classe `<td class="visaoQuadrosTd">`
    '''
    # Abrir o arquivo html
    
    i = 1
    for html_file in file_list:
        print("Abrindo arquivo: ", html_file)
        with open(html_file, "rb") as file:
            bs = bs4.BeautifulSoup(file.read(), 'html.parser')
            
        # Encontra todos os elementos que possuem a classe "visaoQuadrosTd"
        td_elements = bs.find_all(class_="visaoQuadrosTd")

        # Itera sobre os elementos encontrados e extrai as URLs
        for td in td_elements:
            link = td.find('a')
            if link:
                url = link['href']
                #print(url)
                # Salva a URL em um arquivo de texto
                with open("/Volumes/DATA/data_legilacao_brasileira/link_pages/_urls.txt", "a") as file:
                    file.write(url + "\n")
        
        print("Arquivo ", i, " de ", len(file_list), " processado")
        i += 1

    print("Fim do processo")

def parser_codigos():
    '''
    Na link_pages dos Códigos, a classe que contém os links é a class="external-link"
    '''

    # abrir arquivo com códigos brasileiros
    with open("/Volumes/DATA/data_legilacao_brasileira/link_pages/links_codigos.html", "rb") as file:
        bs = bs4.BeautifulSoup(file.read(), 'html.parser')

    # Encontra todos os elementos que possuem a tag "a"
    link_elements = bs.find_all('a', class_="external-link" )

    # Filtra apenas as URLs desejadas (que começam com "http" ou "https")
    urls = [link['href'] for link in link_elements if link.has_attr('href') and link['href'].startswith(('http://www.planalto.gov.br/ccivil_03/', 'https://www.planalto.gov.br/ccivil_03/'))]

    # Itera sobre as URLs encontradas e imprime na tela
    for url in urls:
        #print(url)
        with open("/Volumes/DATA/data_legilacao_brasileira/link_pages/_urls.txt", "a") as file:
            file.write(url + "\n")
    
    print("Arquivo Códigos Brasileiros processado")

def parser_leis_delegadas():
    '''
    Nas `link_pages` de Leis Delegadas, não há classe para identificar os links.
    '''

    # abrir arquivo com códigos brasileiros
    with open("/Volumes/DATA/data_legilacao_brasileira/link_pages/links_leis_delegadas.html", "rb") as file:
        bs = bs4.BeautifulSoup(file.read(), 'html.parser')

    # Encontra todos os elementos que possuem a tag "a"
    link_elements = bs.find_all('a')

    # Filtra apenas as URLs desejadas (que começam com "http" ou "https")
    urls = [link['href'] for link in link_elements if link.has_attr('href') and link['href'].startswith(('https://www.planalto.gov.br/ccivil_03/LEIS/Ldl/'))]

    # Itera sobre as URLs encontradas e imprime na tela
    for url in urls:
        #print(url)
        with open("/Volumes/DATA/data_legilacao_brasileira/link_pages/_urls.txt", "a") as file:
            file.write(url + "\n")
    
    print("Arquivo Leis delegadas processado")


# To do Baixar páginas a partir do link

# Main
if __name__ == "__main__":
    folder = "/Volumes/DATA/data_legilacao_brasileira/link_pages"
    file_list = read_folder_link_pages(folder)
    
    
    parser_link_pages(file_list)

    parser_codigos()

    parser_leis_delegadas()

