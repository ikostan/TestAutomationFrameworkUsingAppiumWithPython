"""Android Calculator App Test: Scientific Notation Conversion"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure

from tests.android_native.calculator_tests.calculator_base_testcase import AndroidCalculatorBaseTestCase


@allure.epic('Android Native App')
@allure.parent_suite('Functional Test')
@allure.suite("Calculator Test Suite")
@allure.sub_suite("Positive Tests")
@allure.feature("Scientific Notation")
@allure.story('Scientific Notation Conversion')
class TestScientificNotationConversionCase(AndroidCalculatorBaseTestCase):
	"""
	Android Calculator App Test: Scientific Notation Conversion

	Convert a number to and scientific notation.
	Enter a number or a decimal number the calculator should convert it to scientific notation format.

	Scientific Notation Converter:
	https://www.calculatorsoup.com/calculators/math/scientific-notation-converter.php
	"""

	def test_scientific_notation_negative(self):
		"""
		1. Enter a digit
		2. Press '=' button
		3. Verify that input is represented with no changes
		:return:
		"""
		allure.dynamic.title("Scientific Notation Conversion test (negative)")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		with allure.step("Clear Calculator screen"):
			self.clear_calculator_screen()

		expected = '1234000000'
		with allure.step("Enter {} digit and tap '='".format(expected)):
			self.enter_digit(expected)
			self.app.equal.tap()

			with allure.step("Verify screen output"):
				assert self.app.screen_result.raw_text == expected

		with allure.step("Clear Calculator screen"):
			self.clear_calculator_screen()

		digit = '34560000456450.0000678679'
		with allure.step("Enter {} digit and tap '='".format(digit)):
			self.enter_digit(digit)
			self.app.equal.tap()

			with allure.step("Verify screen output"):
				assert self.app.screen_result.raw_text == digit

		digit = '345600967890045645000006.78679'
		with allure.step("Enter {} digit and tap '='".format(digit)):
			self.enter_digit(digit)
			self.app.equal.tap()

			with allure.step("Verify screen output"):
				assert self.app.screen_result.raw_text == digit

		with allure.step("Calculate following: 3.45 x 10^5".format(digit)):
			expected_output = '345000'
			self.enter_digit('3.45')
			self.app.multiplication.tap()
			self.enter_digit((10**5))
			self.app.equal.tap()

			with allure.step("Verify screen output"):
				assert self.app.screen_result.raw_text == expected_output

	def test_scientific_notation_positive(self):
		"""
		1. Enter a digit
		2. Press '=' button
		3. Verify scientific notation conversion
		:return:
		"""
		allure.dynamic.title("Scientific Notation Conversion test (positive)")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		with allure.step("Clear Calculator screen"):
			self.clear_calculator_screen()

		digit = '12340000000'
		with allure.step("Enter {} digit and tap '='".format(digit)):
			expected_output = '1.234E10'
			self.enter_digit(digit)
			self.app.equal.tap()

			with allure.step("Verify screen output"):
				assert self.app.screen_result.raw_text == expected_output

		with allure.step("Clear Calculator screen"):
			self.clear_calculator_screen()

		digit = '1234000000000000.0'
		with allure.step("Enter {} digit and tap '='".format(digit)):
			expected_output = '1.234E15'
			self.enter_digit(digit)
			self.app.equal.tap()

			with allure.step("Verify screen output"):
				assert self.app.screen_result.raw_text == expected_output

		with allure.step("Clear Calculator screen"):
			self.clear_calculator_screen()

		digit = '10000000000000000.0'
		with allure.step("Enter {} digit and tap '='".format(digit)):
			expected_output = '1.E16'
			self.enter_digit(digit)
			self.app.equal.tap()

			with allure.step("Verify screen output"):
				assert self.app.screen_result.raw_text == expected_output

		with allure.step("Clear Calculator screen"):
			self.clear_calculator_screen()

		digit = '345600000000'
		with allure.step("Enter {} digit and tap '='".format(digit)):
			expected_output = '3.456E11'
			self.enter_digit(digit)
			self.app.equal.tap()

			with allure.step("Verify screen output"):
				assert self.app.screen_result.raw_text == expected_output

		with allure.step("Clear Calculator screen"):
			self.clear_calculator_screen()

		digit = '3456000000000'
		with allure.step("Enter {} digit and tap '='".format(digit)):
			expected_output = '3.456E12'
			self.enter_digit(digit)
			self.app.equal.tap()

			with allure.step("Verify screen output"):
				assert self.app.screen_result.raw_text == expected_output

		with allure.step("Clear Calculator screen"):
			self.clear_calculator_screen()

		digit = '123456789000000000000000000000'
		with allure.step("Enter {} digit and tap '='".format(digit)):
			expected_output = '1.23456789E29'
			self.enter_digit(digit)
			self.app.equal.tap()

			with allure.step("Verify screen output"):
				assert self.app.screen_result.raw_text == expected_output

		with allure.step("Calculate following: 3.45 x 10^5".format(digit)):
			expected_output = '3.45E10'
			self.enter_digit('3.45')
			self.app.multiplication.tap()
			self.enter_digit((10**10))
			self.app.equal.tap()

			with allure.step("Verify screen output"):
				assert self.app.screen_result.raw_text == expected_output



