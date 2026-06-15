from bs4 import BeautifulSoup



class WikipediaParser:

    def __init__(self, html_content: str):
        self.soup = BeautifulSoup(html_content, 'html.parser')

    def extraer_titulo(self, tema_defecto: str) -> str:

        if not isinstance(tema_defecto, str) or not tema_defecto.strip():
            raise ValueError("tema_defecto debe ser un string no vacío")


        if not self.soup:
            raise ValueError("El objeto soup no está inicializado")

        elemento_titulo = self.soup.find("h1", id="firstHeading")

        if elemento_titulo:
            titulo = elemento_titulo.get_text(strip=True)
            return titulo if titulo else tema_defecto

        return tema_defecto

    def extraer_parrafos(self, cantidad: int = 5):
        contenedor_texto = self.soup.find("div",id="mw-content-text")
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