"""Android Calculator App Test: Division"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
from tests.android_v7_calculator_tests.calculator_base_testcase import AndroidCalculatorBaseTestCase


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
	Should report error for division by 0
	Should be able to divide two many digit floating point numbers
	Should be able to divide the result of a previous operation by a many digit floating point number
	Should be able to divide the result of a previous operation by a large integer

	Source: http://mozilla.github.io/calculator/test/?grep=Unit%20Tests%20Division
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
		with allure.step("Check the division of two positive integers: {}".format(numbers)):
			self.perform_division(numbers)
			assert self.app.screen_result.label == self.eval_formula(1500 / 2000)

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
		with allure.step("Check the division of zero by integer : {}".format(numbers)):
			self.perform_division(numbers)
			assert self.app.screen_result.label == self.eval_formula(0 / 2000)

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
		with allure.step("Check the division of a negative dividend by a positive divisor: {}".format(numbers)):
			self.perform_division(numbers)
			assert self.app.screen_result.label == self.eval_formula(-1500 / 2000)

	def test_divide_a_negative_floating_point_dividend_by_a_positive_divisor(self):
		"""

		:return:
		"""
		allure.dynamic.title("Division of a ")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		#
		numbers = []
		with allure.step("Check the division of : {}".format(numbers)):
			self.perform_division(numbers)
			assert self.app.screen_result.label == self.eval_formula()

	def test_divide_negative_integer_dividend_by_positive_floating_point_divisor_to_nine_significiant_figures(self):
		"""

		:return:
		"""
		allure.dynamic.title("Division of a ")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		#
		numbers = []
		with allure.step("Check the division of : {}".format(numbers)):
			self.perform_division(numbers)
			assert self.app.screen_result.label == self.eval_formula()

	def test_divide_an_floating_point_dividend_by_an_integer_divisor(self):
		"""

		:return:
		"""
		allure.dynamic.title("Division of a ")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		#
		numbers = []
		with allure.step("Check the division of : {}".format(numbers)):
			self.perform_division(numbers)
			assert self.app.screen_result.label == self.eval_formula()

	def test_divide_an_integer_dividend_by_a_floating_point_divisor(self):
		"""

		:return:
		"""
		allure.dynamic.title("Division of a ")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		#
		numbers = []
		with allure.step("Check the division of : {}".format(numbers)):
			self.perform_division(numbers)
			assert self.app.screen_result.label == self.eval_formula()

	def test_divide_two_floating_point_numbers(self):
		"""

		:return:
		"""
		allure.dynamic.title("Division of a ")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		#
		numbers = []
		with allure.step("Check the division of : {}".format(numbers)):
			self.perform_division(numbers)
			assert self.app.screen_result.label == self.eval_formula()

	def test_divide_the_result_of_a_previous_operation_by_a_positive_floating_point_number(self):
		"""

		:return:
		"""
		allure.dynamic.title("Division of a ")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		#
		numbers = []
		with allure.step("Check the division of : {}".format(numbers)):
			self.perform_division(numbers)
			assert self.app.screen_result.label == self.eval_formula()

	def test_divide_the_result_of_a_previous_operation_by_a_positive_integer(self):
		"""

		:return:
		"""
		allure.dynamic.title("Division of a ")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		#
		numbers = []
		with allure.step("Check the division of : {}".format(numbers)):
			self.perform_division(numbers)
			assert self.app.screen_result.label == self.eval_formula()

	def test_report_error_for_division_by_zero(self):
		"""

		:return:
		"""
		allure.dynamic.title("Division of a ")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		#
		numbers = []
		with allure.step("Check the division of : {}".format(numbers)):
			self.perform_division(numbers)
			assert self.app.screen_result.label == self.eval_formula()

	def test_able_to_divide_two_many_digit_floating_point_numbers(self):
		"""

		:return:
		"""
		allure.dynamic.title("Division of a ")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		#
		numbers = []
		with allure.step("Check the division of : {}".format(numbers)):
			self.perform_division(numbers)
			assert self.app.screen_result.label == self.eval_formula()

	def test_able_to_divide_the_result_of_a_previous_operation_by_a_many_digit_floating_point_number(self):
		"""

		:return:
		"""
		allure.dynamic.title("Division of a ")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		#
		numbers = []
		with allure.step("Check the division of : {}".format(numbers)):
			self.perform_division(numbers)
			assert self.app.screen_result.label == self.eval_formula()

	def test_divide_the_result_of_a_previous_operation_by_a_large_integer(self):
		"""

		:return:
		"""
		allure.dynamic.title("Division of a ")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		#
		numbers = []
		with allure.step("Check the division of : {}".format(numbers)):
			self.perform_division(numbers)
			assert self.app.screen_result.label == self.eval_formula()

