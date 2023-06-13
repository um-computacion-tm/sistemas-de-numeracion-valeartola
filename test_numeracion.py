import unittest

from numeracion import numeracion
class TestNumeracion(unittest.TestCase):
    def test_binario2decimal(self):
        self.assertEqual(binario2decimal("0101100"), 96)
    def test_decimal2binario(self):
        self.assertEqual(decimal2roman(97), "01100001")

if __name__ == "__main__":
    unittest.main()