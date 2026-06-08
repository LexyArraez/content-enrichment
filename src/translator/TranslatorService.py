from deep_translator import GoogleTranslator
from deep_translator.exceptions import LanguageNotSupportedException


class TranslatorService:
    def __init__(self):
        pass

    def translate_text(self, text: str, source_lang: str, target_lang: str) :
        if source_lang.strip().lower() == target_lang.strip().lower():
            return text

        try:
            translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
            return translated
        except LanguageNotSupportedException:
            raise ValueError(f"Idioma no soportado: '{target_lang}'.")
        except Exception as e:
            raise RuntimeError(f"Error al traducir el texto: {e}") from e