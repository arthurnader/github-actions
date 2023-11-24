import unittest
from calculator import fatorial, exponenciacao, logaritmo

class TestCalculator(unittest.TestCase):

    def test_fatorial(self):
        self.assertEqual(fatorial(0), 1)
        self.assertEqual(fatorial(1), 1)
        self.assertEqual(fatorial(5), 120)

    def test_exponenciacao(self):
        self.assertEqual(exponenciacao(2, 3), 8)
        self.assertEqual(exponenciacao(5, 0), 1)
        self.assertEqual(exponenciacao(5, -1), 0.2)

    def test_logaritmo(self):
        self.assertEqual(logaritmo(16, 2), 4)
        self.assertEqual(logaritmo(100, 10), 2)

if __name__ == '__main__':
    unittest.main()
