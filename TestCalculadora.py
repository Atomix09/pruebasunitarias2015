import unittest

class TestCalculadora(unittest.TestCase):

	def setUp(self):
		self.calc = Calculadora()

	def test_suma_de_2_mas_2(self):
		
		resultado = self.calc.suma(2,2)

		self.assertEqual(4, resultado)
		
	def test_suma_de_3_mas_3(self):
		
		resultado = self.calc.suma(3,3)

		self.assertEqual(6, resultado)
			
	def test_suma_de_5_mas_5(self):
		
		resultado = self.calc.suma(5,5)

		self.assertEqual(10, resultado)	
	
	def test_resta_de_6_menos_2(self):
		
		resultado = self.calc.resta(6,2)

		self.assertEqual(4, resultado)
		
	def test_multi_4_x_9(self):
		
		resultado = self.calc.multi(4,9)

		self.assertEqual(36, resultado)
	
	def test_multi_15_entre_4(self):
		
		resultado = self.calc.div(15,4)

		self.assertEqual(3, resultado)	

class Calculadora():
	def suma(self,num1,num2):
		return num1+num2
	def resta(self,num1,num2):
		return num1-num2
	def multi(self,num1,num2):
		return num1*num2
	def div(self,num1,num2):
		return num1/num2
		
	


if __name__=="__main__":
	unittest.main()