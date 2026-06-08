import pytest
from unittest.mock import patch, MagicMock
from src.wikipedia.WikipediaClient import WikipediaClient


@pytest.fixture
def cliente_wiki():
    return WikipediaClient()


def test_obtener_html_exitoso(cliente_wiki):
    #  Arrange (Preparar)
    tema = "Python"

    html_esperado = "<html><body>Contenido de Python</body></html>"
    mock_respuesta = MagicMock()
    mock_respuesta.status_code = 200
    mock_respuesta.text = html_esperado

    # Act (Actuar)
    with patch("requests.get", return_value=mock_respuesta) as mock_get:
        resultado_real = cliente_wiki.obtener_html(tema)

    # Assert (Verificar)

    assert resultado_real == html_esperado

    url_esperada = f"{cliente_wiki.BASE_URL}Python"
    mock_get.assert_called_once_with(url_esperada, headers=cliente_wiki.HEADERS)


def test_obtener_html_no_existe_404(cliente_wiki):
    #Arrange
    tema = "Este Tema No Existe"

    mock_respuesta = MagicMock()
    mock_respuesta.status_code = 404

    # Act
    with patch("requests.get", return_value=mock_respuesta):
        with pytest.raises(ValueError) as exc_info:
            cliente_wiki.obtener_html(tema)  # <- Act

        # Assert
        assert f"El tema '{tema}' no existe." in str(exc_info.value)