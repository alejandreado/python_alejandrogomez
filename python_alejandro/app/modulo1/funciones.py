# app/modulo1/funciones.py
"""
funciones.py

Implementa una función robusta llamada esPalindromo que:
- Ignora espacios, puntuación, tildes y mayúsculas.
- Comprueba si la cadena es igual a su reverso.
- Lanza TypeError con entradas no válidas.

También incluye la función auxiliar _normalizar().
"""

import unicodedata
import re

def _normalizar(texto: str) -> str:
    """
    Normaliza una cadena:
    - Elimina acentos y signos diacríticos.
    - Convierte a minúsculas.
    - Elimina todos los símbolos y espacios, dejando solo caracteres alfanuméricos.
    """
    # Descomposición unicode para separar diacríticos
    nfkd = unicodedata.normalize("NFKD", texto)
    
    # Eliminar diacríticos (tildes) 
    sin_diacriticos = ''.join(
        c for c in nfkd if not unicodedata.combining(c)
    )

    # Eliminar cualquier caracter no alfanumérico
    alfanumerico = re.sub(r"[^A-Za-z0-9]", "", sin_diacriticos)

    return alfanumerico.lower()


def esPalindromo(cadena):
    """
    Determina si una cadena es palíndroma.
    Condiciones:
    - None → TypeError
    - No str → TypeError
    - Ignora tildes, espacios, puntuación
    - Devuelve True si tras normalizar es igual a su reverso
    """
    
    if cadena is None:
        raise TypeError("EsPalindromo: se esperaba una cadena, no se recibió nada.")

    if not isinstance(cadena, str):
        raise TypeError("EsPalindromo: la entrada debe ser una cadena de texto.")

    # Quitar espacios iniciales y finales
    cadena = cadena.strip()

    # Si queda vacía, se considera palíndroma
    if cadena == "":
        return True

    normal = _normalizar(cadena)

    # Si tras normalizar no queda nada (solo símbolos), también es palíndroma
    if normal == "":
        return True

    return normal == normal[::-1]
