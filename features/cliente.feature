Feature: Obtener HTML de Wikipedia

  Scenario: Obtener el contenido de un tema existente
    Given existe un artículo llamado "Python"
    When solicito el html del tema
    Then obtengo el contenido de la página
