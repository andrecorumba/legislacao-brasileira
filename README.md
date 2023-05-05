# Legislação Brasileira 

Scripts para download da legislação brasileira constante do site http://www4.planalto.gov.br/legislacao/ 

## Passo a Passo

O passo a passo para efetuar o downaload da legislação brasileira consistiu nas etapadas a segui:

### 1. Download das link pages.
Acessando a página http://www4.planalto.gov.br/legislacao/ é possível observar as classes de legislação, separadas por anos.
Primeiramente criei um conceito denominado *link_pages* ** que se referem às páginas que agrupam links para várias legislações, separadas por anos. Em alguns casos como para *leis delegadas* os links de todas essas leis estão em apenas uma *link_page*.
O código para baixar as *link_pages* de cada tipo de legislação estão em `scripts/link_pages_<legislaçao>.py`.

A função principal para download das link_pages é a `download_link_pages.py` que é chamada pelos outros scrpits individualmente pelos scripts a seguir:

+ constituicao.py
+ link_pages_leis_ordinarias.py
+ link_pages_leis_complementares.py
+ link_pages_decretos.py
+ link_pages_leis_delegadas.py
+ link_pages_codigos.py
+ link_pages_decretos_leis.py
+ link_pages_medidas_provisorias.py
+ link_pages_pecs.py
+ link_pages_estatutos.py
+ link_pages_mensagem_de_veto.py

**OBSERVAÇÕES**

A página da **Constituição Federal** não é *link_page*, mas a própria Constituição em formato `html`.

**Classes que contém os links**

Na `link_pages` dos **Códigos**, obtida em: `http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/codigos-1` a classe que contém os links é a `class="external-link">`

Na `link_pages` de **Leis Delegadas**, obtida em: `http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/leis-delegadas-1`, não há classe para identificar os links.

Nas demais legislações a classe que contém os links é a `<td class="visaoQuadrosTd">`