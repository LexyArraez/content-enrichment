from src.wikipedia.WikipediaScraper import WikipediaScraper


def main():

    print("BIENVENIDA AL CONTENT ENRICHER\n")

    tema_usuario = input("Introduce el tema que deseas investigar en Wikipedia: ")
    idioma_destino = input("Introduce el idioma para la traducción (ej. 'en' para inglés, 'fr' para francés): ")

    if not tema_usuario.strip():
        print("Error: No puedes dejar el tema en blanco.")
        return

    print(f"\nBuscando '{tema_usuario}' en Wikipedia...\n")

    scraper = WikipediaScraper()

    try:
        resultado_wiki = scraper.buscar_tema(tema_usuario)

        print(f"ARTÍCULO ENCONTRADO: {resultado_wiki['titulo']}\n")
        print("Contenido Original de Wikipedia\n")

        for parrafo in resultado_wiki['parrafos']:
            print(f"{parrafo}\n")

        print("Fin del proceso de Scraping con éxito.\n")

    except RuntimeError as error_env:
        print(f"\n[Error de configuración]: {error_env}")
    except ValueError as error:
        print(f"\n[Error de Wikipedia]: {error}")
    except Exception as e:
        print(f"\n[Error Inesperado]: {e}")

if __name__ == "__main__":
   main()