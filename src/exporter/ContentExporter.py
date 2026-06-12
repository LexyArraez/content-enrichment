import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm



class ContentExporter:

    def __init__(self, carpeta_destino: str = "outputs"):

        self.carpeta_destino = carpeta_destino
        if not os.path.exists(self.carpeta_destino):
                os.makedirs(self.carpeta_destino)


    def exportar_txt(self, nombre_archivo: str, contenido: str):
        nombre_archivo = self._validar_nombre(nombre_archivo)
        if not nombre_archivo.endswith(".txt"):
            nombre_archivo += '.txt'

        ruta_completa = os.path.join(self.carpeta_destino, nombre_archivo)

        try:
            with open(ruta_completa, "w", encoding="utf-8") as archivo:
                archivo.write(contenido)
            return ruta_completa

        except Exception as e:
            raise RuntimeError(f"Error al guardar el archivo de texto: {e}")

    def exportar_pdf(self, nombre_archivo: str, tema: str, idioma: str, contenido: str) :
        nombre_archivo = self._validar_nombre(nombre_archivo)
        if not nombre_archivo.endswith(".pdf"):
            nombre_archivo += '.pdf'

        ruta_completa = os.path.join(self.carpeta_destino, nombre_archivo)
        try:
            c = canvas.Canvas(ruta_completa, pagesize=letter)
            ancho, alto = letter

            margen = 2 * cm
            c.drawString(margen, alto - margen, f"Tema: {tema}")
            c.drawString(margen, alto - margen - 20, f"Idioma: {idioma}")

            texto_obj = c.beginText(50, alto - 100)
            texto_obj.setFont("Helvetica", 10)

            for linea in contenido.split("\n"):
                texto_obj.textLine(linea)
            c.drawText(texto_obj)
            c.save()
            return ruta_completa

        except Exception as e:
            raise RuntimeError(f"Error al generar el archivo PDF con Canvas: {e}")

    def _validar_nombre(self, nombre_archivo: str) -> str:
        nombre_archivo = nombre_archivo.strip()
        if not nombre_archivo:
            raise ValueError("El nombre del archivo no puede estar vacío.")
        return nombre_archivo
