"""Android Calculator App Test: Division"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
from tests.android_native.calculator_tests.calculator_base_testcase import AndroidCalculatorBaseTestCase


@allure.epic('Android Native App')
@allure.parent_suite('Functional Test')
@allure.suite("Calculator Test Suite")
@allure.sub_suite("Positive Tests")
@allure.feature("Division Calculation")
@allure.story('Division Button')
class TestDivisionCase(AndroidCalculatorBaseTestCase):
	"""
	Android Calculator App Test: Division
	
	Terminology:
	Dividend / Divisor = quotient
	
	Should be able to divide two positive integers
	Should be able to divide 0 by a integer divisor39ms
	Should be able to divide a negative dividend by a positive divisor
	Should be able to divide a negative floating point dividend by a positive divisor

	Should be able to divide a negative integer dividend by a positive floating
	point divisor to nine significiant figures

	Should be able to divide an floating point dividend by an integer divisor
	Should be able to divide an integer dividend by a floating point divisor
	Should be able to divide two floating point numbers
	Should be able to divide the result of a previous operation by a positive floating point number
	Should be able to divide the result of a previous operation by a positive integer
	Should be able to divide two many digit floating point numbers
	Should be able to divide the result of a previous operation by a many digit floating point number
	Should be able to divide the result of a previous operation by a large integer

	Source: http://mozilla.github.io/calculator/test/
	"""

	def test_divide_two_positive_integers(self):
		"""
		Should be able to divide two positive integers
		1500 / 2000 = 0.75
		:return:
		"""
		allure.dynamic.title("Division of two positive integers test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1500 / 2000 = 0.75
		numbers = [1500, 2000]
		with allure.step("Check the division of two positive integers: 1500 / 2000 = 0.75"):
			self.perform_division(numbers)

			with allure.step("Verify the result"):
				assert self.app.screen_result.formatted_text == self.eval_formula(1500 / 2000)

	def test_divide_zero_by_a_integer_divisor(self):
		"""
		Should be able to divide 0 by a integer divisor
		0 / 2000 = 0
		:return:
		"""
		allure.dynamic.title("Division of a 0 by integer test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 0 / 2000 = 0
		numbers = [0, 2000]
		with allure.step("Check the division of zero by integer : 0 / 2000 = 0"):
			self.perform_division(numbers)

			with allure.step("Verify the result"):
				assert self.app.screen_result.formatted_text == self.eval_formula(0 / 2000)

	def test_divide_a_negative_dividend_by_a_positive_divisor(self):
		"""
		Should be able to divide a negative dividend by a positive divisor
		-1500 / 2000 = -0.75
		:return:
		"""
		allure.dynamic.title("Division of a negative dividend by a positive divisor test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# -1500 / 2000 = -0.75
		numbers = [-1500, 2000]
		with allure.step("Check the division of a negative dividend "
		                 "by a positive divisor: -1500 / 2000 = -0.75"):
			self.perform_division(numbers)

			with allure.step("Verify the result"):
				assert self.app.screen_result.formatted_text == self.eval_formula(-1500 / 2000)

	def test_divide_a_negative_floating_point_dividend_by_a_positive_divisor(self):
		"""
		Should be able to divide a negative floating point dividend by a positive divisor
		-3.123 / 5 = -0.6246
		:return:
		"""
		allure.dynamic.title("Division of a negative floating point dividend by a positive divisor test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# -3.123 / 5 = -0.6246
		numbers = [-3.123, 5]
		with allure.step("Check the division of negative floating point dividend by a "
		                 "positive divisor: -3.123 / 5 = -0.6246"):
			self.perform_division(numbers)

			with allure.step("Verify the result"):
				assert self.app.screen_result.formatted_text == self.eval_formula(-3.123 / 5)

	def test_divide_negative_integer_dividend_by_positive_floating_point_divisor_to_nine_significant_figures(self):
		"""
		Should be able to divide a negative integer dividend by a positive floating point divisor to nine significant figures
		-5 / 3.123 = -1.60102466
		:return:
		"""
		allure.dynamic.title("Division of a a negative integer dividend by a positive "
		                     "floating point divisor to nine significant figures test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# -5 / 3.123 = -1.60102466
		numbers = [-5, 3.123]
		with allure.step("Check the division of a negative integer dividend by a positive "
		                 "floating point divisor to nine significant figures: -5 / 3.123 = -1.60102466"):
			self.perform_division(numbers)

			expected = self.eval_formula(-5 / 3.123)

			with allure.step("Verify the result"):
				assert self.app.screen_result.formatted_text[:len(expected) - 1] == expected[:-1]

	def test_divide_an_floating_point_dividend_by_an_integer_divisor(self):
		"""
		Should be able to divide an floating point dividend by an integer divisor
		4.21 / 3 = 1.40333333
		:return:
		"""
		allure.dynamic.title("Division of floating point dividend by an integer divisor test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 4.21 / 3 = 1.40333333
		numbers = [4.21, 3]
		with allure.step("Check the division of floating point dividend "
		                 "by an integer divisor: 4.21 / 3 = 1.40333333"):
			self.perform_division(numbers)

			expected = self.eval_formula(4.21 / 3)

			with allure.step("Verify the result"):
				assert self.app.screen_result.formatted_text[:len(expected) - 1] == expected[:-1]

	def test_divide_an_integer_dividend_by_a_floating_point_divisor(self):
		"""
		Should be able to divide an integer dividend by a floating point divisor
		10 / 3.123 = 3.20204931
		:return:
		"""
		allure.dynamic.title("Division of a integer dividend by a floating point divisor test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 10 / 3.123 = 3.20204931
		numbers = [10, 3.123]
		with allure.step("Check the division of integer dividend by a "
		                 "floating point divisor: 10 / 3.123 = 3.20204931"):
			self.perform_division(numbers)

			expected = self.eval_formula(10 / 3.123)

			with allure.step("Verify the result"):
				assert self.app.screen_result.formatted_text[:len(expected) - 1] == expected[:-1]

	def test_divide_two_floating_point_numbers(self):
		"""
		Should be able to divide two floating point numbers
		0.234 / 3.123 = 0.0749279539
		:return:
		"""
		allure.dynamic.title("Division of two floating point numbers")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 0.234 / 3.123 = 0.0749279539
		numbers = [0.234, 3.123]
		with allure.step("Check the division of two floating point numbers: 0.234 / 3.123 = 0.0749279539"):
			self.perform_division(numbers)

			expected = self.eval_formula(0.234 / 3.123)

			with allure.step("Verify the result"):
				assert self.app.screen_result.formatted_text[:len(expected) - 1] == expected[:-1]

	def test_divide_the_result_of_a_previous_operation_by_a_positive_floating_point_number(self):
		"""
		Should be able to divide the result of a previous operation by a positive floating point number
		1500 - 2000 = 500 / 3.12 = -160.25641
		:return:
		"""
		allure.dynamic.title("Division of the result of a previous operation "
		                     "by a positive floating point number test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1500 - 2000 = 500 / 3.12 = -160.25641
		with allure.step("Check the division of the result of a previous operation "
		                 "by a positive floating point number: 1500 - 2000 = 500 / 3.12 = "):
			self.enter_digit(1500)
			self.app.minus.tap()
			self.enter_digit(2000)
			self.app.equal.tap()
			self.enter_digit(500)
			self.app.division.tap()
			self.enter_digit(3.12)
			self.app.equal.tap()

			expected = self.eval_formula(500 / 3.12)

			with allure.step("Verify the result"):
				assert self.app.screen_result.formatted_text[:len(expected) - 1] == expected[:-1]

	def test_divide_the_result_of_a_previous_operation_by_a_positive_integer(self):
		"""
		Should be able to divide the result of a previous operation by a positive integer
		1500 - 2000 = 500 / 312 = -1.6025641
		6 * 2 = 12 / 8 = 1.5
		:return:
		"""
		allure.dynamic.title("Division of the result of a previous "
		                     "operation by a positive integer test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1500 - 2000 = 500 / 312 = -1.6025641
		with allure.step("Check the division of the result of a previous "
		                 "operation by a positive integer: 1500 - 2000 = 500 / 312 = -1.6025641"):
			self.enter_digit(1500)
			self.app.minus.tap()
			self.enter_digit(2000)
			self.app.equal.tap()
			self.enter_digit(500)
			self.app.division.tap()
			self.enter_digit(312)
			self.app.equal.tap()

			expected = str(500 / 312)

			with allure.step("Verify the result"):
				assert self.app.screen_result.formatted_text[:len(expected) - 1] == expected[:-1]

		# 6 * 2 = 12 / 8 = 1.5
		with allure.step("Check the division of the result of a previous "
		                 "operation by a positive integer: 6 * 2 = 12 / 8 = 1.5"):
			self.enter_digit(6)
			self.app.minus.tap()
			self.enter_digit(2)
			self.app.equal.tap()
			self.enter_digit(12)
			self.app.division.tap()
			self.enter_digit(8)
			self.app.equal.tap()

			expected = self.eval_formula(12 / 8)

			with allure.step("Verify the result"):
				assert self.app.screen_result.formatted_text[:len(expected) - 1] == expected[:-1]

	def test_able_to_divide_two_many_digit_floating_point_numbers(self):
		"""
		Should be able to divide two many digit floating point numbers
		1.23456789 / 2.10987654 = 0.585137503
		:return:
		"""
		allure.dynamic.title("Division of two many digit floating point numbers test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1.23456789 / 2.10987654 = 0.585137503
		numbers = [1.23456789, 2.10987654]
		with allure.step("Check the division of two many digit floating point numbers: 1.23456789 / 2.10987654"):
			self.perform_division(numbers)

			expected = self.eval_formula(1.23456789 / 2.10987654)

			with allure.step("Verify the result"):
				assert self.app.screen_result.formatted_text[:len(expected) - 1] == expected[:-1]

	def test_able_to_divide_the_result_of_a_previous_operation_by_a_many_digit_floating_point_number(self):
		"""
		Should be able to divide the result of a previous operation by a many digit floating point number
		1500 - 2000 = -500 / 1234.56789 = -0.405000004
		:return:
		"""
		allure.dynamic.title("Division of the result of a previous operation "
		                     "by a many digit floating point number test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1500 - 2000 = -500 / 1234.56789 = -0.405000004
		with allure.step("Check the division of the result of a previous operation "
		                 "by a many digit floating point number: 1500 - 2000 + (-500 / 1234.56789)"):
			self.enter_digit(1500)
			self.app.minus.tap()
			self.enter_digit(2000)
			self.app.equal.tap()
			self.enter_digit(-500)
			self.app.division.tap()
			self.enter_digit(1234.56789)
			self.app.equal.tap()

			expected = self.eval_formula(1500 - 2000 + (-500 / 1234.56789))

			with allure.step("Verify the result"):
				assert self.app.screen_result.formatted_text[:len(expected) - 1] == expected[:-1]

	def test_divide_the_result_of_a_previous_operation_by_a_large_integer(self):
		"""
		Should be able to divide the result of a previous operation by a large integer
		1500 - 2000 = -500 / 123456789 = -0.00000405000004
		:return:
		"""
		allure.dynamic.title("Division of the result of a previous "
		                     "operation by a large integer test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1500 - 2000 = -500 / 123456789 = -0.00000405000004
		with allure.step("Check the division of the result of a previous "
		                 "operation by a large integer: -500 - (500 / 123456789)"):
			self.enter_digit(1500)
			self.app.minus.tap()
			self.enter_digit(2000)
			self.app.equal.tap()
			self.enter_digit(-500)
			self.app.division.tap()
			self.enter_digit(123456789)
			self.app.equal.tap()

			expected = str(-500 - (500 / 123456789))

			with allure.step("Verify the result"):
				assert self.app.screen_result.formatted_text[:len(expected) - 1] == expected[:-1]

