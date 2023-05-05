from download_link_pages import download_link_pages
import os

if __name__ == "__main__":
    #link_pages_medidas_provisorias()
    folder = "/Volumes/DATA/data_legilacao_brasileira/link_pages"
    url = "http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/estatutos"
    download_css_class_name = "external-link"

    #find_link_pages(url, type_of_law, css_class_name, download_css_class_name)
    download_link_pages(url,os.path.join(folder, "links_estatutos.html"), download_css_class_name )