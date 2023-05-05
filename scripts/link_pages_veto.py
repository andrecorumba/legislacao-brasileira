from download_link_pages import find_link_pages
    
if __name__ == "__main__":
    #link_pages_medidas_provisorias()
    url = "http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/mensagem-de-veto-total"
    type_of_law = "veto"
    css_class_name = "internal-link"
    download_css_class_name = "external-link"

    find_link_pages(url, type_of_law, css_class_name, download_css_class_name)