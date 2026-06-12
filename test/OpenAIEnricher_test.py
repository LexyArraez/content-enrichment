import os
import pytest
from unittest.mock import patch, MagicMock
from src.enricher.OpenAIEnricher import OpenAIEnricher


def test_enriquecer_texto_exitoso():
    mock_respuesta = MagicMock()
    mock_respuesta.choices = [
        MagicMock(message=MagicMock(content="Texto enriquecido de prueba."))
    ]

    with patch.dict(os.environ, {"GROQ_API_KEY": "clave_falsa"}):
        with patch("openai.resources.chat.completions.Completions.create", return_value=mock_respuesta):
            enricher = OpenAIEnricher()
            resultado = enricher.enrich_text("Python", ["Es un lenguaje", "Es popular"])

            assert resultado == "Texto enriquecido de prueba."


def test_inicializar_sin_api_key():

    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(RuntimeError) as error:
            OpenAIEnricher()

        assert str(error.value) == "La variable GROQ_API_KEY no se encontró en el archivo .env"

