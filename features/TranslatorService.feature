Feature: Traduccion de texto

  Scenario: Traduccion correcta entre dos idiomas diferentes
    Given tengo el texto "Hello" en idioma "en"
    When traduzco al idioma "es"
    Then obtengo una traduccion no vacia

  Scenario: El texto no se traduce si origen y destino son el mismo idioma
    Given tengo el texto "Hola" en idioma "es"
    When traduzco al idioma "es"
    Then obtengo el mismo texto "Hola" sin llamar al API

  Scenario: Se lanza un error si el idioma no existe
    Given tengo el texto "Hello" en idioma "en"
    When traduzco al idioma "xx"
    Then obtengo un ValueError con el mensaje "Idioma no soportado: 'xx'."