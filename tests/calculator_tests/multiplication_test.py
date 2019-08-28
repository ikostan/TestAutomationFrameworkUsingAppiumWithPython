"""Android Calculator App Test: Multiplication"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
from tests.calculator_tests.calculator_base_testcase import AndroidCalculatorBaseTestCase


@allure.epic('Android Native App')
@allure.parent_suite('Functional Test')
@allure.suite("Calculator Test Suite")
@allure.sub_suite("Positive Tests")
@allure.feature("Multiplication Calculation")
@allure.story('Multiplication Button')
class TestMultiplicationCase(AndroidCalculatorBaseTestCase):
	"""
	Android Calculator App Test: Multiplication
	
	Terminology:
	Multiplicand * Multiplier = Product
	
	Should be able to multiply two positive integers 
	Should be able to multiply a floating point multiplicand with an integer multipliplier40ms 
	Should be able to multiply an integer multiplicand with a floating point multiplier 
	Should be able to multiply two floating point numbers 
	Should be able to multiply a integer multiplicand with zero 
	Should be able to multiply a negative integer multiplicand with a positive intger multiplier 
	Should be able to multiply a negative floating point multiplicand with a positive integer multiplier 
	Should be able to multiply a negative integer multiplicand with a positive floating point multiplier 
	Should be able to multiply the result of a previous operation by a positive floating point number 
	Should be able to multiply the result of a previous operation by a positive integer 
	Should be able to multiply two many digit floating point numbers 
	Should be able to multiply two large integers 
	Should be able to multiply the result of a previous operation by large integer 
	Should be able to multiply the result of a previous operation by a many digit floating point number 
	Should be able to result of a previous operation when the previous result is zero

	Source: https://mozilla.github.io/calculator/test/?grep=Unit%20Tests%20Addition
	"""

	def test_multiply_two_positive_integers(self):
		"""
		Should be able to multiply two positive integers
		1500 * 2000 = 3000000
		:return: 
		"""
		allure.dynamic.title("Multiply two positive integers test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1500 * 2000 = 3000000
		numbers = [1500, 2000]
		with allure.step("Check the multiplication of two positive integers: {}".format(numbers)):
			self.perform_multiplication(numbers)
			assert self.app.screen_result.label == self.eval_formula(1500 * 2000)

	def test_multiply_a_floating_point_multiplicand_with_an_integer_multipliplier(self):
		"""
		Should be able to multiply a floating point multiplicand with an integer multipliplier:
		1.212 * 8 = 9.696
		:return: 
		"""
		allure.dynamic.title("Multiplication of a floating point multiplicand "
		                     "with an integer multipliplier test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1.212 * 8 = 9.696
		numbers = [1.212, 8]
		with allure.step("Check the multiplication of a floating point "
		                 "multiplicand with an integer multipliplier: {}".format(numbers)):
			self.perform_multiplication(numbers)
			assert self.app.screen_result.label == self.eval_formula(1.212 * 8)

	def test_multiply_an_integer_multiplicand_with_a_floating_point_multiplier(self):
		"""
		Should be able to multiply an integer multiplicand with a floating point multiplier
		3 * 1.212 = 3.636
		:return: 
		"""
		allure.dynamic.title("Multiplication an integer multiplicand "
		                     "with a floating point multiplier test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 3 * 1.212 = 3.636
		numbers = [3, 1.212]
		with allure.step("Check the multiplication of an integer "
		                 "multiplicand with a floating point multiplier: {}".format(numbers)):
			self.perform_multiplication(numbers)
			assert self.app.screen_result.label == self.eval_formula(3 * 1.212)

	def test_multiply_two_floating_point_numbers(self):
		"""
		Should be able to multiply two floating point numbers
		0.133 * 1.212 = 0.161196
		:return: 
		"""
		allure.dynamic.title("Multiply of two floating point numbers test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 0.133 * 1.212 = 0.161196
		numbers = [0.133, 1.212]
		with allure.step("Check the multiplication of two floating point numbers: {}".format(numbers)):
			self.perform_multiplication(numbers)
			assert self.app.screen_result.label == self.eval_formula(0.133 * 1.212)

	def test_multiply_a_integer_multiplicand_with_zero(self):
		"""
		Should be able to multiply a integer multiplicand with zero
		1500 * 0 = 0
		:return: 
		"""
		allure.dynamic.title("Multiplication of a integer multiplicand with zero test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1500 * 0 = 0
		numbers = [1500, 0]
		with allure.step("Check the multiplication of a integer multiplicand with zero: {}".format(numbers)):
			self.perform_multiplication(numbers)
			assert self.app.screen_result.label == self.eval_formula(1500 * 0)

	def test_multiply_a_negative_integer_multiplicand_with_a_positive_intger_multiplier(self):
		"""
		Should be able to multiply a negative integer multiplicand with a positive intger multiplier
		-1500 * 2000 = -3000000
		:return: 
		"""
		allure.dynamic.title("Multiplication of a negative integer multiplicand "
		                     "with a positive integer multiplier test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# -1500 * 2000 = -3000000
		numbers = [-1500, 2000]
		with allure.step("Check the multiplication of a negative integer multiplicand "
		                 "with a positive intger multiplier: {}".format(numbers)):
			self.perform_multiplication(numbers)
			assert self.app.screen_result.label == self.eval_formula(-1500 * 2000)

	def test_multiply_a_negative_floating_point_multiplicand_with_a_positive_integer_multiplier(self):
		"""
		Should be able to multiply a negative floating point multiplicand with a positive integer multiplier
		-1.212 * 8 = -9.696
		:return: 
		"""
		allure.dynamic.title("Multiplication of a negative floating point multiplicand "
		                     "with a positive integer multiplier test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# -1.212 * 8 = -9.696
		numbers = [-1.212, 8]
		with allure.step("Check the multiplication of a negative floating point multiplicand "
		                 "with a positive integer multiplier: {}".format(numbers)):
			self.perform_multiplication(numbers)
			assert self.app.screen_result.label == self.eval_formula(-1.212 * 8)

	def test_multiply_a_negative_integer_multiplicand_with_a_positive_floating_point_multiplier(self):
		"""
		Should be able to multiply a negative integer multiplicand with a positive floating point multiplier
		-8 * 1.212 = -9.696
		:return: 
		"""
		allure.dynamic.title("multiplication of a negative integer multiplicand with "
		                     "a positive floating point multiplier test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# -8 * 1.212 = -9.696
		numbers = [-8, 1.212]
		with allure.step("Check the multiplication of a negative integer "
		                 "multiplicand with a positive floating point multiplier: {}".format(numbers)):
			self.perform_multiplication(numbers)
			assert self.app.screen_result.label == self.eval_formula(-8 * 1.212)

	def test_multiply_the_result_of_a_previous_operation_by_a_positive_floating_point_number(self):
		"""
		Should be able to multiply the result of a previous operation by a positive floating point number
		1500 - 2000 = -500 * 1.23 = -615
		:return: 
		"""
		allure.dynamic.title("Multiplication of the result of a previous "
		                     "operation by a positive floating point number test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1500 - 2000 = -500 * 1.23 = -615
		numbers = [1500, 2000, -500, 1.23]
		with allure.step("Check the multiplication of the result of a previous "
		                 "operation by a positive floating point number: {}".format(numbers)):
			self.enter_number(1500)
			self.app.minus.tap()
			self.enter_number(2000)
			self.app.equal.tap()
			self.enter_number(-500)
			self.app.multiplication.tap()
			self.enter_number(1.23)
			self.app.equal.tap()
			assert self.app.screen_result.label == self.eval_formula(1500 - 2000 + (-500 * 1.23))

	def test_multiply_the_result_of_a_previous_operation_by_a_positive_integer(self):
		"""
		Should be able to multiply the result of a previous operation by a positive integer
		1500 - 2000 = -500 * 123 = -61500
		6 * 2 = 12 * 8 = 96
		:return: 
		"""
		allure.dynamic.title("Multiplication of the result of a previous "
		                     "operation by a positive integer test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1500 - 2000 = -500 * 123 = -61500
		numbers = [1500, 2000, -500, 123]
		with allure.step("Check the multiplication of the result of a previous "
		                 "operation by a positive integer: {}".format(numbers)):
			self.enter_number(1500)
			self.app.minus.tap()
			self.enter_number(2000)
			self.app.equal.tap()
			self.enter_number(-500)
			self.app.multiplication.tap()
			self.enter_number(123)
			self.app.equal.tap()
			assert self.app.screen_result.label == self.eval_formula(1500 - 2000 + (-500 * 123))

		# 6 * 2 = 12 * 8 = 96
		numbers = [6, 2, 12, 8]
		with allure.step("Check the multiplication of the result of a previous "
		                 "operation by a positive integer: {}".format(numbers)):
			self.enter_number(6)
			self.app.minus.tap()
			self.enter_number(2)
			self.app.equal.tap()
			self.enter_number(12)
			self.app.multiplication.tap()
			self.enter_number(8)
			self.app.equal.tap()
			assert self.app.screen_result.label == self.eval_formula(12 * 8)

	def test_multiply_two_many_digit_floating_point_numbers(self):
		"""
		Should be able to multiply two many digit floating point numbers
		1.23456789 * 2.10987654 = 2.60478583
		:return: 
		"""
		allure.dynamic.title("Multiplication of two many digit floating point numbers test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1.23456789 * 2.10987654 = 2.60478583
		numbers = [1.23456789, 2.10987654]
		with allure.step("Check the multiplication of two many digit floating point numbers: {}".format(numbers)):
			self.perform_multiplication(numbers)
			assert '%.13f'.format(self.app.screen_result.label) == '%.13f'.format(1.23456789 * 2.10987654)

	def test_multiply_two_large_integers(self):
		"""
		Should be able to multiply two large integers
		123456789 * 210987654 = 2.60478583e+16
		:return: 
		"""
		allure.dynamic.title("Multiplication of two large integers")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 
		numbers = [123456789, 210987654]
		with allure.step("Check the multiplication of two large integers: {}".format(numbers)):
			self.perform_multiplication(numbers)
			assert self.app.screen_result.label == self.eval_formula(123456789 * 210987654)

	def test_multiply_the_result_of_a_previous_operation_by_large_integer(self):
		"""
		Should be able to multiply the result of a previous operation by large integer
		1500 - 2000 = -500 * 123456789 = -6.17283945e+10
		:return: 
		"""
		allure.dynamic.title("Multiplication of the result of a previous operation by large integer test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1500 - 2000 = -500 * 123456789 = -6.17283945e+10
		numbers = [1500, 2000, -500, 123456789]
		with allure.step("Check the multiplication of the result of a "
		                 "previous operation by large integer: {}".format(numbers)):
			self.enter_number(1500)
			self.app.minus.tap()
			self.enter_number(2000)
			self.app.equal.tap()
			self.enter_number(-500)
			self.app.multiplication.tap()
			self.enter_number(123456789)
			self.app.equal.tap()
			assert self.app.screen_result.label == self.eval_formula(1500 - 2000 + (-500 * 123456789))

	def test_multiply_the_result_of_a_previous_operation_by_a_many_digit_floating_point_number(self):
		"""
		Should be able to multiply the result of a previous operation by a many digit floating point number
		1500 - 2000 = -500 * 123.456789 = -61728.3945
		:return: 
		"""
		allure.dynamic.title("Multiplication the result of a previous operation "
		                     "by a many digit floating point number test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1500 - 2000 = -500 * 123.456789 = -61728.3945
		numbers = [1500, 2000, -500, 123.456789]
		with allure.step("Check the multiplication of the result of a previous operation "
		                 "by a many digit floating point number: {}".format(numbers)):
			self.enter_number(1500)
			self.app.minus.tap()
			self.enter_number(2000)
			self.app.equal.tap()
			self.enter_number(-500)
			self.app.multiplication.tap()
			self.enter_number(123.456789)
			self.app.equal.tap()
			assert self.app.screen_result.label == self.eval_formula(1500 - 2000 + (-500 * 123.456789))

	def test_multiply_result_of_a_previous_operation_when_the_previous_result_is_zero(self):
		"""
		Should be able multiply to result of a previous operation when the previous result is zero
		0 * 6 * 6 = 0
		:return: 
		"""
		allure.dynamic.title("Multiply to result of a previous operation when the "
		                     "previous result is zero test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 0 * 6 * 6 = 0
		numbers = [0, 6, 6]
		with allure.step("Check the multiplication of result of a "
		                 "previous operation when the previous result is zero: {}".format(numbers)):
			self.perform_multiplication(numbers)
			assert self.app.screen_result.label == self.eval_formula(0 * 6 * 6)
