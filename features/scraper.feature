Feature: Extracción de contenido de Wikipedia

  Scenario: Obtener exitosamente los párrafos de un tema
    Given  parser de Wikipedia tiene listo un listado de párrafos de prueba
    When el scraper busca la información de un tema
    Then el resultado debe contener exactamente esos párrafos de prueba
