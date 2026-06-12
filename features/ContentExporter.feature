Feature: Exportacion de contenido a archivos

  Scenario: Exportar contenido a un archivo de texto de forma exitosa
    Given que tengo el exportador de contenido listo
    When solicito exportar un archivo TXT con el nombre "archivo_facil_test" y contenido "Hola Mundo"
    Then el archivo se guarda correctamente en el disco con la extension ".txt"

  Scenario: Exportar contenido a un archivo PDF usando Canvas de forma exitosa
    Given que tengo el exportador de contenido listo
    When solicito exportar un archivo PDF con el nombre "pdf_facil_test", tema "Prueba", idioma "es" y contenido "Texto del PDF"
    Then el archivo se guarda correctamente en el disco con la extension ".pdf"

  Scenario: Intentar exportar un archivo TXT sin asignarle un nombre
    Given que tengo el exportador de contenido listo
    When solicito exportar un archivo TXT con el nombre "   " y contenido "Contenido"
    Then se lanza un ValueError con el mensaje "El nombre del archivo no puede estar vacio."
