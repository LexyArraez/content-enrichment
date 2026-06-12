Feature: Enriquecimiento de texto con IA

  Scenario: Enriquecer contenido de forma exitosa
    Given que tengo la clave GROQ_API_KEY configurada en el entorno
    When solicito enriquecer el tema "Python" con los parrafos "Es un lenguaje" y "Es popular"
    Then obtengo un texto enriquecido en español con maximo 5 parrafos

  Scenario: Intentar inicializar el servicio sin la clave de la API
    Given que la variable GROQ_API_KEY no existe en el archivo env
    When intento inicializar el modulo OpenAIEnricher
    Then se lanza un RuntimeError con el mensaje "La variable GROQ_API_KEY no se encontro en el archivo .env"