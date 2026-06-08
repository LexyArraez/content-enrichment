import pathlib
import requests
from dotenv import dotenv_values


RUTA_RAIZ = pathlib.Path(__file__).resolve().parent.parent.parent
RUTA_ENV = RUTA_RAIZ / ".env"


config = dotenv_values(RUTA_ENV)

class WikipediaClient:

    BASE_URL = config.get("WIKIPEDIA_BASE_URL")
    HEADERS = {"User-Agent": config.get("WIKIPEDIA_USER_AGENT")}

    def obtener_html(self, tema: str):

        if not self.BASE_URL:
            raise RuntimeError(
                "Error de configuración: No se pudo leer la variable WIKIPEDIA_BASE_URL. "
            )
        tema_formateado = tema.strip().replace(" ", "_")
        try:
            respuesta = requests.get(f"{self.BASE_URL}{tema_formateado}", headers=self.HEADERS)
            if respuesta.status_code == 404:
                raise ValueError(f"El tema '{tema}' no existe.")
            respuesta.raise_for_status()
            return respuesta.text
        except requests.RequestException as e:
            raise RuntimeError(f"Error de red: {e}")