# Content Enrichment Tool 

Una herramienta automatizada en Python diseñada para extraer información de Wikipedia, enriquecerla utilizando Inteligencia Artificial (a través de la API de Groq/OpenAI con modelos Llama 3) y exportar el resultado final tanto en archivos de texto plano (`.txt`) como en documentos PDF profesionales y estructurados (`.pdf`).

---

##  Características del Proyecto

* **Wikipedia Client & Scraper:** Busca y extrae de manera limpia el contenido HTML de cualquier tema directamente desde Wikipedia, gestionando las excepciones de páginas no encontradas.
* **AI Content Enricher:** Conecta con modelos avanzados de lenguaje a través de la API de Groq para expandir el texto original, aportando mayor contexto, ejemplos y datos de valor.
* **Translator Service:** Traduce los contenidos enriquecidos al idioma final configurado, optimizando los recursos si los idiomas de origen y destino coinciden.
* **Content Exporter:** Genera las salidas del software en archivos legibles, aplicando filtros de limpieza de nombres y controlando errores de guardado con ReportLab Canvas.

---

##  Tecnologías y Requisitos

El ecosistema de dependencias necesario para ejecutar y validar el desarrollo incluye:

## Dependencias

| Librería | Uso |
|---|---|
| `requests` | Peticiones HTTP a APIs y Wikipedia |
| `beautifulsoup4` | Scraping del HTML de Wikipedia |
| `reportlab` | Generación de archivos PDF |
| `pytest` | Tests unitarios e integración |
| `OpenAI SDK` | Consumo del servicio de Inteligencia Artificial de Groq |

---

##  Instalación y Uso Local 

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local desde la terminal de PyCharm:

bash
### 1. Clona el repositorio y accede a la carpeta
git clone [https://github.com/LexyArraez/content-enrichment.git]
cd content-enrichment

### 2. Instala las dependencias necesarias en tu entorno virtual (.venv)
pip install -r requirements.txt

### 3. Configura las variables de entorno
 Crea un archivo .env en la raíz del proyecto y añade tu API key de Groq
GROQ_API_KEY=tu_clave_api_aqui_sin_comillas


## Uso

bash
python main.py

---

## El programa guiará al usuario paso a paso:

1. Introduce el tema a investigar
2. Elige el idioma de traducción
3. Decide si quieres un resumen con AI
4. Elige el nombre del archivo
5. Elige el formato de salida (`txt` o `pdf`)
---


## 📂 Estructura Real del Proyecto

La arquitectura del repositorio sigue una división modular rígida orientada a componentes independientes:

```text
content-enrichment/
│
├── .venv/                        # Entorno virtual con las librerías del proyecto
│
├── features/                     # Especificaciones de comportamiento (Gherkin BDD)
│   ├── ContentExporter.feature
│   ├── OpenAIEnricher.feature
│   ├── TranslatorService.feature
│   ├── WikipediaClient.feature
│   └── WikipediaScraper.feature
│
├── outputs/                      # Carpeta local autogenerada para almacenar las salidas (.txt y .pdf)
│
├── src/                          # Código fuente de la aplicación
│   ├── cli/                      # Interfaz de línea de comandos del programa
│   ├── enricher/                 # Lógica de conexión con IA (Groq/OpenAI)
│   ├── exporter/                 # Lógica de exportación de archivos (Canvas PDF/TXT)
│   ├── translator/               # Lógica de traducción de contenidos
│   ├── utils/                    # Funciones y utilidades secundarias reutilizables
│   └── wikipedia/                # Lógica del cliente HTTP y parsing de Wikipedia
│
├── test/                         # Suite de Pruebas Automatizadas con Pytest
│   ├── ContentExporter_test.py   # Cobertura del exportador de archivos
│   ├── OpenAIEnricher_test.py    # Cobertura de llamadas simuladas de IA
│   ├── TranslatorService_test.py # Cobertura de traducción y validación de códigos
│   ├── WikipediaClient_test.py   # Cobertura del cliente HTTP de Wikipedia
│   └── WikipediaScraper_test.py  # Cobertura del parser extractor de HTML
│
├── .env                          # Archivo de variables de entorno (Oculto / Claves API)
├── .env.example                  # Plantilla de ejemplo pública para variables locales
├── .gitignore                    # Reglas de exclusión de Git (Evita subir .env y .venv)
├── main.py                       # Orquestador y punto de entrada principal del programa
└── requirements.txt              # Listado de paquetes congelados para su instalación ```






