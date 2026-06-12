import pytest
from src.translator.TranslatorService import TranslatorService


def test_traduccion_correcta_entre_idiomas_diferentes():

    servicio = TranslatorService()
    texto_origen = "Hello"

    resultado = servicio.translate_text(text=texto_origen, source_lang="en", target_lang="es")

    assert resultado is not None
    assert len(resultado.strip()) > 0



def test_no_traduce_si_es_el_mismo_idioma():
    servicio = TranslatorService()
    texto_origen = "Hola"

    resultado = servicio.translate_text(text=texto_origen, source_lang="es", target_lang="es")

    assert resultado == "Hola"

def test_idioma_no_soportado_lanza_value_error():

    servicio = TranslatorService()

    with pytest.raises(ValueError) as informacion_error:
        servicio.translate_text(text="Hello", source_lang="en", target_lang="xx")

    assert str(informacion_error.value) == "Idioma no soportado: 'xx'"