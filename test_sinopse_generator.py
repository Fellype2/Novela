import unittest
from sinopse_generator import gerar_sinopse

class TestGerarSinopse(unittest.TestCase):
    def test_estrutura_retorno(self):
        resultado = gerar_sinopse()
        self.assertIsInstance(resultado, dict)
        self.assertIn("título", resultado)
        self.assertIn("tema", resultado)
        self.assertIn("local", resultado)
        self.assertIn("sinopse", resultado)

if __name__ == "__main__":
    unittest.main()
