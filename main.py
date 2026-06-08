from src.wikipedia.WikipediaScraper import WikipediaScraper


def main():
    scraper = WikipediaScraper()

    print("BIENVENIDA AL CONTENT ENRICHER\n")

    tema_usuario = input("Introduce el tema que deseas investigar en Wikipedia: ")
    if not tema_usuario.strip():
        print("Error: El tema no puede estar vacío.")
        return

    idioma_usuario = input("Ingrese el código del idioma de destino:").strip().lower() or "es"


    try:
        print("Conectando con Wikipedia y traduciendo contenido... Por favor, espere.\n")
        resultado = scraper.buscar_tema(tema_usuario, idioma_usuario)

        print(f"TÍTULO TRADUCIDO ({idioma_usuario.upper()}): {resultado['titulo']}\n")

        for parrafo in resultado['parrafos']:
            print(parrafo + "\n")


        print("Contenido obtenido y traducido con éxito.\n")
        input("Presione [ENTER] para cerrar la aplicación...")


    except ValueError as e:
        print(f"\nError de validación: {e}")
        input("\nPresione [ENTER] para salir...")
    except RuntimeError as e:
        print(f"\nError al traducir: {e}")
        input("\nPresione [ENTER] para salir...")
    except Exception as e:
        print(f"\nOcurrió un problema inesperado: {e}")
        input("\nPresione [ENTER] para salir...")



if __name__ == "__main__":
   main()