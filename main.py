from src.wikipedia.scraper import WikipediaScraper


def main():


    print("BIENVENIDA AL CONTENT ENRICHER\n")

    tema_usuario = input("Introduce el tema que deseas investigar en Wikipedia: ")

    if not tema_usuario.strip():
        print("Error: No puedes dejar el tema en blanco.")
        return

    print(f"\nBuscando '{tema_usuario}' en Wikipedia...\n")

    scraper = WikipediaScraper()

    try:
        resultado_wiki = scraper.buscar_tema(tema_usuario)

        print(f"ARTÍCULO ENCONTRADO: {resultado_wiki['titulo']}\n")

        for parrafo in resultado_wiki['parrafos']:
            print(f"{parrafo}\n")


        print("Fin del proceso de Scraping con éxito.")

    except ValueError as error:
        print(f"\nHa ocurrido un problema: {error}")

if __name__ == "__main__":
   main()