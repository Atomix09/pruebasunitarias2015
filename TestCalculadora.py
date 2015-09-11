import unittest

class TestCalculadora(unittest.TestCase):

	def test_suma_de_2_mas_2(self):
		calc = Calculadora()
		
		resultado = calc.suma(2,2)

		self.assertEqual(4, resultado)

if __name__=="__main__":
	unittest.main()