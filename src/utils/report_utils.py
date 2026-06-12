import re


def limpiar_markdown(texto: str) -> str:
    texto = re.sub(r'\*\*(.*?)\*\*', r'\1', texto)
    texto = re.sub(r'\*(.*?)\*', r'\1', texto)
    return texto.strip()


def construir_reporte(tema: str,idioma: str,titulo: str,parrafos: list,texto_enriquecido: str,texto_traducido: str):

    texto_original = "\n\n".join(parrafos)

    enriquecido_limpio = limpiar_markdown(texto_enriquecido)
    traducido_limpio = limpiar_markdown(texto_traducido)

    return (
        f"=== REPORTE GENERADO: {tema.upper()} ===\n\n"
        f"--- 1. CONTENIDO ORIGINAL DE WIKIPEDIA ---\n"
        f"Título: {titulo}\n\n"
        f"{texto_original}\n\n"
        f"--- 2. CONTENIDO ENRIQUECIDO POR IA ---\n\n"
        f"{enriquecido_limpio}\n\n"
        f"--- 3. CONTENIDO TRADUCIDO FINAL ({idioma.upper()}) ---\n\n"
        f"{traducido_limpio}"
    )