import os
import pytest
from src.exporter.ContentExporter import ContentExporter


def test_guardar_archivo_texto_funciona():

    exporter = ContentExporter()

    ruta = exporter.exportar_txt("archivo_test", "Hola Mundo")

    assert os.path.exists(ruta)
    assert ruta.endswith(".txt")


def test_guardar_archivo_pdf_funciona():
    exporter = ContentExporter()


    ruta = exporter.exportar_pdf("pdf_test", "Prueba", "es", "Texto del PDF")

    assert os.path.exists(ruta)
    assert ruta.endswith(".pdf")


def test_error_si_nombre_archivo_vacio():
    exporter = ContentExporter()


    with pytest.raises(ValueError) as error:
        exporter.exportar_txt("   ", "Contenido")
        exporter.exportar_pdf("   ", "Contenido")

    assert str(error.value) == "El nombre del archivo no puede estar vacío."
