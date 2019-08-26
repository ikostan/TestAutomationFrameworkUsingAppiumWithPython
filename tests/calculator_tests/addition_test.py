"""Calculator App Test Case: Addition"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
from tests.calculator_tests.base_testcase import BaseTestCase


@allure.epic('Android Native App')
@allure.parent_suite('End To End')
@allure.suite("Calculator Test Suite")
@allure.sub_suite("Positive Tests")
@allure.feature("Addition Calculation")
@allure.story('Addition Button')
class TestAdditionCase(BaseTestCase):

	"""
	This suite tests the current code in the calculator_test.
	Any tests that fail will be in red text with a red x and tests that pass will have a green check mark.
	You can click on the text for any case to see what test code is being run.
	The code can be read in rough English to understand what is being tested.

	Terminology
	Addend + Addend = Sum
	Minuend - Subtrahend = Difference
	Multiplicand * Multiplier = Product
	Dividend / Divisor = quotient
	calculator_test Test Suite

	Should be able to add two positive integers numbers ‣
	Should be able to add a negative integer to a positive floating point number ‣
	Should be able to add a floating point number to an integer ‣
	Should be able to add an integer to a floating point number ‣
	Should be able to add two floating point numbers ‣
	Should be able to add a negative integer and zero ‣
	Should be able to add zero and a positive integer ‣
	Should be able to add a negative integer with a positive number ‣
	Should be able to add two large positive integers ‣
	Should be able to add a negative floating point and a positive integer ‣
	Should be able to add a positive integer to the results of a previous operation ‣
	Should be able to add a positive floating point number to the results of a previous operation ‣
	Should be able to add a floating point number with many decimal places to a previous result ‣
	Should be able to add a large integer to a previous result

	Source: https://mozilla.github.io/calculator/test/?grep=Unit%20Tests%20Addition
	"""

	def test_able_to_add_two_positive_integers(self):
		"""
		Should be able to add two positive integers numbers ‣
		:return:
		"""
		allure.dynamic.title("")
		allure.dynamic.severity(allure.severity_level.BLOCKER)
		pass

	def test_able_to_add_a_negative_integer_to_a_positive_floating_point_number(self):
		"""
		Should be able to add a negative integer to a positive floating point number
		:return:
		"""
		allure.dynamic.title("")
		allure.dynamic.severity(allure.severity_level.BLOCKER)
		pass

	def test_able_to_add_a_floating_point_number_to_an_integer(self):
		"""
		Should be able to add a floating point number to an integer
		:return:
		"""
		allure.dynamic.title("")
		allure.dynamic.severity(allure.severity_level.BLOCKER)
		pass

	def test_able_to_add_an_integer_to_a_floating_point_number(self):
		"""
		Should be able to add an integer to a floating point number
		:return:
		"""
		allure.dynamic.title("")
		allure.dynamic.severity(allure.severity_level.BLOCKER)
		pass

	def test_able_to_add_two_floating_point_numbers(self):
		"""
		Should be able to add two floating point numbers
		:return:
		"""
		allure.dynamic.title("")
		allure.dynamic.severity(allure.severity_level.BLOCKER)
		pass

	def test_able_to_add_a_negative_integer_and_zero(self):
		"""
		Should be able to add a negative integer and zero
		:return:
		"""
		allure.dynamic.title("")
		allure.dynamic.severity(allure.severity_level.BLOCKER)
		pass

	def test_able_to_add_zero_and_a_positive_integer(self):
		"""
		Should be able to add zero and a positive integer
		:return:
		"""
		allure.dynamic.title("")
		allure.dynamic.severity(allure.severity_level.BLOCKER)
		pass

	def test_able_to_add_a_negative_integer_with_a_positive_number(self):
		"""
		Should be able to add a negative integer with a positive number
		:return:
		"""
		allure.dynamic.title("")
		allure.dynamic.severity(allure.severity_level.BLOCKER)
		pass

	def test_able_to_add_two_large_positive_integers(self):
		"""
		Should be able to add two large positive integers
		:return:
		"""
		allure.dynamic.title("")
		allure.dynamic.severity(allure.severity_level.BLOCKER)
		pass

	def test_able_to_add_a_negative_floating_point_and_a_positive_integer(self):
		"""
		Should be able to add a negative floating point and a positive integer
		:return:
		"""
		allure.dynamic.title("")
		allure.dynamic.severity(allure.severity_level.BLOCKER)
		pass

	def test_able_to_add_a_positive_integer_to_the_results_of_a_previous_operation(self):
		"""
		Should be able to add a positive integer to the results of a previous operation
		:return:
		"""
		allure.dynamic.title("")
		allure.dynamic.severity(allure.severity_level.BLOCKER)
		pass

	def test_able_to_add_a_positive_floating_point_number_to_the_results_of_a_previous_operation(self):
		"""
		Should be able to add a positive floating point number to the results of a previous operation
		:return:
		"""
		allure.dynamic.title("")
		allure.dynamic.severity(allure.severity_level.BLOCKER)
		pass

	def test_able_to_add_a_floating_point_number_with_many_decimal_places_to_a_previous_result(self):
		"""
		Should be able to add a floating point number with many decimal places to a previous result
		:return:
		"""
		allure.dynamic.title("")
		allure.dynamic.severity(allure.severity_level.BLOCKER)
		pass

	def test_able_to_add_a_large_integer_to_a_previous_result(self):
		"""
		Should be able to add a large integer to a previous result
		:return:
		"""
		allure.dynamic.title("")
		allure.dynamic.severity(allure.severity_level.BLOCKER)
		pass

