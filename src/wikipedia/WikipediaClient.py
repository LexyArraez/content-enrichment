import requests


class WikipediaClient:

    BASE_URL = "https://es.wikipedia.org/wiki/"
    HEADERS = {"User-Agent": "MiPrimerScraperBot/1.0"}

    def obtener_html(self, tema: str) -> str:
        tema_formateado = tema.strip().replace(" ", "_")
        url_completa = f"{self.BASE_URL}{tema_formateado}"

        try:
            respuesta = requests.get(url_completa, headers=self.HEADERS)

            if respuesta.status_code == 404:
                raise ValueError(f"¡Vaya! El tema '{tema}' no existe en Wikipedia.")

            respuesta.raise_for_status()
            return respuesta.text

        except requests.RequestException as e:
            raise RuntimeError(f"Error de conexión al buscar '{tema}': {e}")