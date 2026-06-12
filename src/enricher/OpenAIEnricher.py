import os
import openai
from dotenv import load_dotenv

load_dotenv()

class OpenAIEnricher:

    def __init__(self):

        api_key_groq = os.getenv("GROQ_API_KEY")

        if not api_key_groq:
            raise RuntimeError("La variable GROQ_API_KEY no se encontró en el archivo .env")

        self.client = openai.OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=api_key_groq.strip()
        )

    def enrich_text(self, titulo: str, parrafos: list):
        prompt = "Enriquece el contenido añadiendo contexto, ejemplos y datos relevantes en español y en máximo 5 párrafos"
        texto_completo = f"Título: {titulo}\n\n" + "\n\n".join(parrafos)

        respuesta = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": texto_completo}
            ]
        )
        return respuesta.choices[0].message.content