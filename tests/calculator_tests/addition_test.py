"""Calculator App Test: Addition"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
from tests.calculator_tests.base_testcase import BaseTestCase


@allure.epic('Android Native App')
@allure.parent_suite('Functional Test')
@allure.suite("Calculator Test Suite")
@allure.sub_suite("Positive Tests")
@allure.feature("Addition Calculation")
@allure.story('Addition Button')
class TestAdditionCase(BaseTestCase):

	"""
	This suite tests the current code in the calculator.

	Terminology
	Addend + Addend = Sum

	Test Suite List:

	Should be able to add two positive integers numbers
	Should be able to add a negative integer to a positive floating point number
	Should be able to add a floating point number to an integer
	Should be able to add an integer to a floating point number
	Should be able to add two floating point numbers
	Should be able to add a negative integer and zero
	Should be able to add zero and a positive integer
	Should be able to add a negative integer with a positive number
	Should be able to add two large positive integers
	Should be able to add a negative floating point and a positive integer
	Should be able to add a positive integer to the results of a previous operation
	Should be able to add a positive floating point number to the results of a previous operation
	Should be able to add a floating point number with many decimal places to a previous result
	Should be able to add a large integer to a previous result

	Source: https://mozilla.github.io/calculator/test/?grep=Unit%20Tests%20Addition
	"""

	def test_able_to_add_two_positive_integers(self):
		"""
		Should be able to add two positive integers numbers and display the result

		Steps:
		1. Key in a valid integer from - 9999999999 to +9999999999
		2. Key in operator +
		3. Key in second operand,a valid integer from - 9999999999 To +999999999
		4. Result verification > check the screen output

		Source: https://www.ques10.com/p/38809/prepare-and-write-six-test-cases-for-simple-calcul/?
		:return:
		"""
		allure.dynamic.title("Add two positive integers numbers and display the result")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# Should be able to add two positive integers numbers

		numbers = [1, 1]
		with allure.step("Check the addition of integer numbers: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == str(sum(numbers))

		numbers = [1, 9]
		with allure.step("Check the addition of integer numbers: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == str(sum(numbers))

		numbers = [19, 2]
		with allure.step("Check the addition of integer numbers: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == str(sum(numbers))

		numbers = [19, 37]
		with allure.step("Check the addition of integer numbers: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == str(sum(numbers))

		numbers = [1500, 2000]
		with allure.step("Check the addition of integer numbers: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == str(sum(numbers))

		numbers = [999999, 1]
		with allure.step("Check the addition of integer numbers: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == str(sum(numbers))

		numbers = [9999999, 1]
		with allure.step("Check the addition of integer numbers: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [99999999, 1]
		with allure.step("Check the addition of integer numbers: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [999999999, 1]
		with allure.step("Check the addition of integer numbers: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [9999999999, 1]
		with allure.step("Check the addition of integer numbers: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

	def test_able_to_add_a_negative_integer_to_a_positive_floating_point_number(self):
		"""
		Should be able to add a negative integer to a positive floating point number
		:return:
		"""
		allure.dynamic.title("Add a negative integer to a positive floating point number")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		numbers = [-1, 1.000]
		with allure.step("Check the addition of negative integer to a positive floating point number: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [-2, 1.000]
		with allure.step(
				"Check the addition of negative integer to a positive floating point number: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [-1, 2.000]
		with allure.step(
				"Check the addition of negative integer to a positive floating point number: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

	def test_able_to_add_a_floating_point_number_to_an_integer(self):
		"""
		Should be able to add a floating point number to an integer
		:return:
		"""
		allure.dynamic.title("Add a floating point number to an integer")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		numbers = [10.1, 2]
		with allure.step(
				"Check the addition of floating point number to an integer: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [10.000, 2]
		with allure.step(
				"Check the addition of floating point number to an integer: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [0.0, 2]
		with allure.step(
				"Check the addition of floating point number to an integer: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

	def test_able_to_add_an_integer_to_a_floating_point_number(self):
		"""
		Should be able to add an integer to a floating point number
		:return:
		"""
		allure.dynamic.title("Add an integer to a floating point number")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		numbers = [10, 9.9999]
		with allure.step(
				"Check the addition of an integer to a floating point number: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [9, 10.9999]
		with allure.step(
				"Check the addition of an integer to a floating point number: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

	def test_able_to_add_two_floating_point_numbers(self):
		"""
		Should be able to add two floating point numbers
		:return:
		"""
		allure.dynamic.title("Add two floating point numbers")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		numbers = [34.999, 1.0]
		with allure.step(
				"Check the addition of two floating point numbers: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [1.0, 34.999]
		with allure.step(
				"Check the addition of two floating point numbers: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [1.0000, 34.999]
		with allure.step(
				"Check the addition of two floating point numbers: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

	def test_able_to_add_a_negative_integer_and_zero(self):
		"""
		Should be able to add a negative integer and zero
		:return:
		"""
		allure.dynamic.title("Add a negative integer and zero")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		numbers = [0, -5]
		with allure.step(
				"Check the addition of negative integer and zero: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [-5, 0]
		with allure.step(
				"Check the addition of negative integer and zero: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [5, -0]
		with allure.step(
				"Check the addition of negative integer and zero: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [-0, 5]
		with allure.step(
				"Check the addition of negative integer and zero: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

	def test_able_to_add_zero_and_a_positive_integer(self):
		"""
		Should be able to add zero and a positive integer
		:return:
		"""
		allure.dynamic.title("Add zero and a positive integer")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		numbers = [0, 0]
		with allure.step("Check the addition of zero and a positive integer: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [0, 1]
		with allure.step("Check the addition of zero and a positive integer: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [1, 0]
		with allure.step("Check the addition of zero and a positive integer: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [0, 5]
		with allure.step("Check the addition of zero and a positive integer: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

	def test_able_to_add_a_negative_integer_with_a_positive_number(self):
		"""
		Should be able to add a negative integer with a positive number
		:return:
		"""
		allure.dynamic.title("Add a negative integer with a positive number")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		numbers = [-5, 5]
		with allure.step("Check the addition of a negative integer with a positive number: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [5, -5]
		with allure.step("Check the addition of a negative integer with a positive number: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [6, -5]
		with allure.step("Check the addition of a negative integer with a positive number: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [-6, 5]
		with allure.step("Check the addition of a negative integer with a positive number: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

	def test_able_to_add_two_large_positive_integers(self):
		"""
		Should be able to add two large positive integers
		:return:
		"""
		allure.dynamic.title("Add two large positive integers")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		numbers = [999999, 999999]
		with allure.step("Check the addition of integer numbers: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [999999, 99999]
		with allure.step("Check the addition of integer numbers: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [99999, 99999]
		with allure.step("Check the addition of integer numbers: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [53645567, 78967875]
		with allure.step("Check the addition of integer numbers: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [9999999999, 567457362343241]
		with allure.step("Check the addition of integer numbers: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [300000000, 900000000]
		with allure.step("Check the addition of integer numbers: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [900000000, 900000000]
		with allure.step("Check the addition of integer numbers: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [999999999, 1]
		with allure.step("Check the addition of integer numbers: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

	def test_able_to_add_a_negative_floating_point_and_a_positive_integer(self):
		"""
		Should be able to add a negative floating point and a positive integer
		:return:
		"""
		allure.dynamic.title("Add a negative floating point and a positive integer")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		numbers = [-1987.50, 1987]
		with allure.step("Check the addition of negative floating point and a positive integer: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		numbers = [1987, -1987.50]
		with allure.step("Check the addition of negative floating point and a positive integer: {}".format(numbers)):
			self.perform_addition(numbers)
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

	def test_able_to_add_a_positive_integer_to_the_results_of_a_previous_operation(self):
		"""
		Should be able to add a positive integer to the results of a previous operation
		:return:
		"""
		allure.dynamic.title("Add a positive integer to the results of a previous operation")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1500 - 2000 = -500 + 500 = 0
		numbers = [1500, -2000, -500, 500]
		with allure.step("Check the addition of positive integer to the results of a previous operation: {}".format(numbers)):
			self.enter_number(numbers[0])
			self.app.plus.tap()
			self.enter_number(numbers[1])
			self.app.plus.tap()
			self.enter_number(numbers[2])
			self.app.plus.tap()
			self.enter_number(numbers[3])
			self.app.equal.tap()
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

		# 6 * 2 + 8 = 20
		numbers = [6, 2, 8]
		with allure.step("Check the addition of positive integer to the results of a previous operation: {}".format(numbers)):
			self.enter_number(numbers[0])
			self.app.multiplication.tap()
			self.enter_number(numbers[1])
			self.app.plus.tap()
			self.enter_number(numbers[2])
			self.app.equal.tap()
			assert self.app.screen_result.label == self.eval_formula(6 * 2 + 8)

	def test_able_to_add_a_positive_floating_point_number_to_the_results_of_a_previous_operation(self):
		"""
		Should be able to add a positive floating point number to the results of a previous operation
		:return:
		"""
		allure.dynamic.title("Add a positive floating point number to the results of a previous operation")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1500 - 2000 = -500 + 0.25 = -999.75
		numbers = [1500, -2000, -500, 0.25]
		with allure.step(
				"Check that user is able to add a positive floating point "
				"number to the results of a previous operation: {}".format(numbers)):
			self.enter_number(numbers[0])
			self.app.plus.tap()
			self.enter_number(numbers[1])
			self.app.plus.tap()
			self.enter_number(numbers[2])
			self.app.plus.tap()
			self.enter_number(numbers[3])
			self.app.equal.tap()
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

	def test_able_to_add_a_floating_point_number_with_many_decimal_places_to_a_previous_result(self):
		"""
		Should be able to add a floating point number with many decimal places to a previous result
		:return:
		"""
		allure.dynamic.title("Add a floating point number with many decimal places to a previous result")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1500 - 2000 = -500 + 1.23456789 = -998.765432
		numbers = [1500, -2000, -500, 1.23456789]
		with allure.step(
				"Check that user is able to add a floating point number with many decimal "
				"places to a previous result: {}".format(numbers)):
			self.enter_number(numbers[0])
			self.app.plus.tap()
			self.enter_number(numbers[1])
			self.app.plus.tap()
			self.enter_number(numbers[2])
			self.app.plus.tap()
			self.enter_number(numbers[3])
			self.app.equal.tap()
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))

	def test_able_to_add_a_large_integer_to_a_previous_result(self):
		"""
		Should be able to add a large integer to a previous result
		:return:
		"""
		allure.dynamic.title("Add a large integer to a previous result")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1500 - 2000 = -500 + 123456789 = 123456289
		numbers = [1500, -2000, -500, 123456789]
		with allure.step(
				"Check that user is able to add a floating point number with many decimal "
				"places to a previous result: {}".format(numbers)):
			self.enter_number(numbers[0])
			self.app.plus.tap()
			self.enter_number(numbers[1])
			self.app.plus.tap()
			self.enter_number(numbers[2])
			self.app.plus.tap()
			self.enter_number(numbers[3])
			self.app.equal.tap()
			assert self.app.screen_result.label == self.eval_formula(sum(numbers))
