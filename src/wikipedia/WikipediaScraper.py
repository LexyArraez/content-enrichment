from src.wikipedia.WikipediaClient import WikipediaClient
from src.wikipedia.WikipediaParser import WikipediaParser
from src.translator.TranslatorService import TranslatorService


class WikipediaScraper:

    def __init__(self):
        self.cliente = WikipediaClient()
        self.traductor = TranslatorService()

    def buscar_tema(self, tema: str ,idioma_destino: str = "es"):

        html = self.cliente.obtener_html(tema)

        parser = WikipediaParser(html)
        titulo = parser.extraer_titulo(tema)
        parrafos = parser.extraer_parrafos(cantidad=5)

        titulo_traducido = self.traductor.translate_text(
            titulo, source_lang='es', target_lang=idioma_destino
        )

        parrafos_traducidos = [
            self.traductor.translate_text(p, source_lang='es', target_lang=idioma_destino)
            for p in parrafos
        ]
        return {"titulo": titulo_traducido, "parrafos": parrafos_traducidos}