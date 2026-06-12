from src.wikipedia.WikipediaScraper import WikipediaScraper
from src.enricher.OpenAIEnricher import OpenAIEnricher
from src.translator.TranslatorService import TranslatorService
from src.exporter.ContentExporter import ContentExporter
from src.utils.report_utils import construir_reporte


def pedir_inputs_usuario() -> tuple[str, str]:

    tema = input(
        "Introduce el tema que deseas investigar en Wikipedia: "
    ).strip()

    if not tema:
        raise ValueError("El tema no puede estar en blanco.")

    idioma = input(
        "Introduce el idioma para la traducción "
        "(ej. 'en', 'fr'): "
    ).strip()

    return tema, idioma


def obtener_contenido_wikipedia(tema: str) -> dict:

    scraper = WikipediaScraper()

    resultado = scraper.buscar_tema(tema)

    print(f"\nARTÍCULO ENCONTRADO: {resultado['titulo']}\n")
    print("CONTENIDO ORIGINAL DE WIKIPEDIA\n")

    for parrafo in resultado["parrafos"]:
        print(f"{parrafo}\n")

    print("Fin del proceso de Scraping con éxito.\n")

    return resultado


def enriquecer_contenido(resultado_wiki: dict) -> str:

    input(
        "Presiona ENTER para enviar el contenido "
        "a la IA y enriquecer el texto..."
    )

    print("\nIniciando el enriquecimiento del texto...\n")

    enricher = OpenAIEnricher()

    texto = enricher.enrich_text(
        titulo=resultado_wiki["titulo"],
        parrafos=resultado_wiki["parrafos"]
    )

    print("CONTENIDO ENRIQUECIDO POR IA\n")
    print(texto)

    return texto


def traducir_contenido(
    texto_enriquecido: str,
    idioma: str
) -> str:

    input(
        "\nPresiona ENTER para traducir el contenido..."
    )

    print(f"\nTraduciendo al idioma '{idioma}'...\n")

    translator = TranslatorService()

    texto_traducido = translator.translate_text(
        text=texto_enriquecido,
        source_lang="es",
        target_lang=idioma
    )

    print("CONTENIDO TRADUCIDO\n")
    print(texto_traducido)

    return texto_traducido


def pedir_configuracion_exportacion(
    tema: str
) -> tuple[str, str]:

    print("CONFIGURACIÓN DE LA GENERACIÓN DE ARCHIVOS\n")

    nombre_archivo = input(
        "\nIntroduce el NOMBRE para tu archivo "
    ).strip()

    nombre_archivo = nombre_archivo.strip()
    if not nombre_archivo:
        raise ValueError("El nombre del archivo no puede estar vacío.")

    print("\nSeleccione el formato de guardado:")
    print("1. Archivo TXT")
    print("2. Documento PDF")

    opcion = input("Elige una opción (1 o 2) ").strip()

    return nombre_archivo, opcion


def exportar_reporte(tema: str,idioma: str,nombre_archivo: str,opcion_formato: str,reporte: str):
    exporter = ContentExporter()
    print("\nGenerando archivo...")

    if opcion_formato == "2":

        exporter.exportar_pdf(
            nombre_archivo=nombre_archivo,
            tema=tema,
            idioma=idioma,
            contenido=reporte
        )

    else:
        exporter.exportar_txt(
            nombre_archivo=nombre_archivo,
            contenido=reporte
        )

    print("\n¡Archivo generado con éxito!")
    print("Se ha guardado en la carpeta del proyecto.")


def iniciar():

    print("BIENVENIDA AL CONTENT ENRICHER\n")

    try:

        tema, idioma = pedir_inputs_usuario()

        print(f"\nBuscando '{tema}' en Wikipedia...\n")

        resultado_wiki = obtener_contenido_wikipedia(
            tema
        )

        texto_enriquecido = enriquecer_contenido(
            resultado_wiki
        )

        texto_traducido = traducir_contenido(
            texto_enriquecido,
            idioma
        )

        nombre_archivo, opcion_formato = (
            pedir_configuracion_exportacion(tema)
        )

        reporte = construir_reporte(
            tema=tema,
            idioma=idioma,
            titulo=resultado_wiki["titulo"],
            parrafos=resultado_wiki["parrafos"],
            texto_enriquecido=texto_enriquecido,
            texto_traducido=texto_traducido
        )

        exportar_reporte(
            tema,
            idioma,
            nombre_archivo,
            opcion_formato,
            reporte
        )

    except RuntimeError as e:
        print(f"\n[Error de configuración]: {e}")

    except ValueError as e:
        print(f"\n[Error]: {e}")

    except Exception as e:
        print(f"\n[Error inesperado]: {e}")