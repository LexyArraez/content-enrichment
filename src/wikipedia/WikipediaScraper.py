from src.wikipedia.WikipediaClient import WikipediaClient
from src.wikipedia.WikipediaParser import WikipediaParser
from src.translator.TranslatorService import TranslatorService


class WikipediaScraper:

    def __init__(self):
        self.cliente = WikipediaClient()

    def buscar_tema(self, tema: str ,idioma_destino: str = "es"):

        html = self.cliente.obtener_html(tema)

        parser = WikipediaParser(html)
        titulo = parser.extraer_titulo(tema)
        parrafos = parser.extraer_parrafos(cantidad=5)


        return {"titulo": titulo, "parrafos": parrafos}