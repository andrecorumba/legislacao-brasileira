# CONTINUIÇÃO FEDERAL

# Script para baixar a Constituição Federal

# Importar bibliotecas
import requests
import os


def constituicao(destination_folder):
    # Definir URL
    url = 'http://www.planalto.gov.br/ccivil_03/Constituicao/Constituicao.htm'

    # Separa o nome do arquivo da URL
    filename = url.split('/')[-1]
    
    # Baixar o arquivo
    print("Baixando arquivo: {}".format(filename))

    # Necessário incluir o cabeçalho de agente de usuário
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)

    print(response.status_code)

    # Salvar o arquivo
    with open(os.path.join(destination_folder, filename), 'wb') as f:
        f.write(response.content)

def main():
    # Definir pasta de destino
    destination_folder = '/Volumes/DATA/data_legilacao_brasileira/html'
    
    # Criar pasta de destino, se não existir
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)

    # Baixar a Constituição Federal
    constituicao(destination_folder)
    print("Constituição Federal baixada com sucesso!")

if __name__ == '__main__':
    main()