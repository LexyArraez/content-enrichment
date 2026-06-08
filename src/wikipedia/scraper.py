from src.wikipedia.cliente import WikipediaClient
from src.wikipedia.parser import WikipediaParser


class WikipediaScraper:

    def __init__(self):
        self.cliente = WikipediaClient()

    def buscar_tema(self, tema: str):

        html = self.cliente.obtener_html(tema)

        parser = WikipediaParser(html)
        titulo = parser.extraer_titulo(tema)
        parrafos = parser.extraer_parrafos(cantidad=5)


        return {
            "titulo": titulo,
            "parrafos": parrafos
        }