from bs4 import BeautifulSoup



class WikipediaParser:

    def __init__(self, html_content: str):
        self.soup = BeautifulSoup(html_content, 'html.parser')

    def extraer_titulo(self, tema_defecto: str):
        elemento_titulo = self.soup.find(id="firstHeading")
        return elemento_titulo.text if elemento_titulo else tema_defecto

    def extraer_parrafos(self, cantidad: int = 5):
        contenedor_texto = self.soup.find(id="mw-content-text")
        if not contenedor_texto:
            return []

        parrafos_limpios = []
        todos_los_parrafos = contenedor_texto.find_all('p')

        for p in todos_los_parrafos:
            texto = p.get_text().strip()
            if texto:
                parrafos_limpios.append(texto)

            if len(parrafos_limpios) == cantidad:
                break

        return parrafos_limpios