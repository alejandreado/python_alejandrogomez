# tests/test_palindromo.py
"""
Pruebas para la función esPalindromo.
Cubre:
- Palíndromos simples
- Con acentos
- Con símbolos
- Con números
- Casos no palíndromos
- Entradas inválidas
- Cadenas vacías y casos límite
"""

import unittest
from app.modulo1.funciones import esPalindromo

class TestEsPalindromo(unittest.TestCase):

    def test_palindromos_simples(self):
        casos = [
            ("Ana", True),
            ("ala", True),
            ("A man, a plan, a canal: Panama", True),
            ("No 'x' in Nixon", True),
        ]
        for entrada, esperado in casos:
            with self.subTest(entrada=entrada):
                self.assertEqual(esPalindromo(entrada), esperado)

    def test_con_acentos(self):
        casos = [
            ("ÁnA", True),
            ("Dábale arroz a la zorra el abad", True),
            ("Sé verás", False),
        ]
        for entrada, esperado in casos:
            with self.subTest(entrada=entrada):
                self.assertEqual(esPalindromo(entrada), esperado)

    def test_numeros_y_signos(self):
        casos = [
            ("12321", True),
            ("12.321", True),
            ("1 2 3 2 1", True),
            ("12345", False)
        ]
        for entrada, esperado in casos:
            with self.subTest(entrada=entrada):
                self.assertEqual(esPalindromo(entrada), esperado)

    def test_cadenas_vacias_o_signos(self):
        self.assertTrue(esPalindromo(""))
        self.assertTrue(esPalindromo("    "))
        self.assertTrue(esPalindromo("!!!"))
        self.assertTrue(esPalindromo(".,,,.,.,."))

    def test_entradas_invalidas(self):
        with self.assertRaises(TypeError):
            esPalindromo(None)
        with self.assertRaises(TypeError):
            esPalindromo(123)
        with self.assertRaises(TypeError):
            esPalindromo(["hola"])

if __name__ == "__main__":
    unittest.main()