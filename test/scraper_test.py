from src.wikipedia.WikipediaScraper import WikipediaScraper


def mi_cliente_vacio(tema):
    return "html"

def mi_titulo_vacio(self, tema):
    return "Título"

def mis_parrafos_de_prueba(self, cantidad):
    return ["Párrafo de prueba 1", "Párrafo de prueba 2"]


def test_scraper_obtiene_los_parrafos_correctos():
    # Arrange
    scraper = WikipediaScraper()

    scraper.cliente.obtener_html = mi_cliente_vacio

    from src.wikipedia.WikipediaParser import WikipediaParser
    WikipediaParser.extraer_titulo = mi_titulo_vacio

    WikipediaParser.extraer_parrafos = mis_parrafos_de_prueba

    # Act

    resultado = scraper.buscar_tema("Cualquier Tema")

    # Assert
    assert resultado["parrafos"] == ["Párrafo de prueba 1", "Párrafo de prueba 2"]