import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self):
        self.base_url = "https://es.wikipedia.org/wiki/"
        self.headers = {
            "User-Agent": "MiPrimerScraperBot/1.0"
        }
    def buscar_tema(self, tema: str):
        tema_formateado = tema.strip().replace(" ", "_")
        url_completa = f"{self.base_url}{tema_formateado}"
        respuesta = requests.get(url_completa, headers=self.headers)

        if respuesta.status_code == 404:
            raise ValueError(f"¡Vaya! El tema '{tema}' no existe en Wikipedia.")

        soup = BeautifulSoup(respuesta.text, 'html.parser')
        elemento_titulo = soup.find(id="firstHeading")
        titulo = elemento_titulo.text if elemento_titulo else tema

        contenedor_texto = soup.find(id="mw-content-text")
        parrafos_limpios = []
        if contenedor_texto:
            todos_los_parrafos = contenedor_texto.find_all('p')

            for p in todos_los_parrafos:
                texto = p.get_text().strip()
                if texto:
                    parrafos_limpios.append(texto)

                if len(parrafos_limpios) == 5:
                    break
        return {
            "titulo": titulo,
            "parrafos": parrafos_limpios
        }