"""Android Calculator App Test: Bad Input"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
from tests.android_v7.calculator_tests.calculator_base_testcase import AndroidCalculatorBaseTestCase


@allure.epic('Android Native App')
@allure.parent_suite('Functional Test')
@allure.suite("Calculator Test Suite")
@allure.sub_suite("Negative Tests")
@allure.feature("Invalid Scenarios")
@allure.story('Bad Input')
class TestBadInputCase(AndroidCalculatorBaseTestCase):
	"""
	Android Calculator App Test: Bad Input

	Should treat an initial press of the decimal mark as "0."
	Should not allow multiple zeros as input
	Should not allow multiple zeros before a decimal mark
	Should not allow a zero before another digit of input
	Should ignore zero before another digit of input for a second operand
	Should allow floating point input with multiple digits before and after the decimal mark
	Should allow a first decimal operand to display a leading zero
	Should allow the second decimal operand to display a leading zero
	Should allow floating point input with a single digit before and after the decimal mark
	Should not count a decimal mark against max input
	Should not allow a double negation
	Should allow the maximum input when the first digit is zero

	Source: https://mozilla.github.io/calculator/test/
	"""

	def test_treatment_an_initial_press_of_the_decimal_mark(self):
		"""
		Should treat an initial press of the decimal mark as "0."
		.11111 -> = -> 0.1111
		:return:
		"""
		allure.dynamic.title("Treat an initial press of the decimal mark as '0.' test")
		allure.dynamic.severity(allure.severity_level.MINOR)

		with allure.step("Enter following: .11111 ="):
			self.app.dot.tap()
			self.app.digits[1].tap()
			self.app.equal.tap()
			assert self.app.screen_result.label == '0.1'

	def test_allow_multiple_zeros_as_input(self):
		"""
		Should not allow multiple zeros as input
		0000 -> 0
		:return:
		"""
		allure.dynamic.title("Should not allow multiple zeros as input test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		with allure.step("Enter following: 0000 = "):
			self.app.digits[0].tap()
			self.app.digits[0].tap()
			self.app.digits[0].tap()
			self.app.digits[0].tap()
			self.app.equal.tap()
			assert self.app.screen_result.label == '0'

	def test_allow_multiple_zeros_before_a_decimal_mark(self):
		"""
		Should not allow multiple zeros before a decimal mark
		000.11111 -> 0.11111
		:return:
		"""
		allure.dynamic.title("Should not allow multiple zeros before a decimal mark test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		with allure.step("Enter following: 000.11111 = "):
			self.enter_digit('000.11111')
			self.app.equal.tap()
			assert self.app.screen_result.label == '0.11111'

	def test_allow_a_zero_before_another_digit_of_input(self):
		"""
		Should not allow a zero before another digit of input
		06 -> 6
		:return:
		"""
		allure.dynamic.title("Should not allow a zero before another digit of input test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		with allure.step("Enter following: 06 = "):
			self.enter_digit('06')
			self.app.equal.tap()
			assert self.app.screen_result.label == '6'

	def test_allow_a_zero_before_another_digit_of_input_for_a_second_operand(self):
		"""
		Should ignore zero before another digit of input for a second operand
		6 * 06 -> 6
		:return:
		"""
		allure.dynamic.title("Should ignore zero before another digit of input for a second operand test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		with allure.step("Enter following: 6 * 06 = "):
			self.enter_digit(6)
			self.app.multiplication.tap()
			self.enter_digit('06')
			self.app.equal.tap()

			with allure.step("Check the result"):
				assert self.app.screen_result.label == '36'

	def test_allow_floating_point_input_with_multiple_digits_before_and_after_the_decimal_mark(self):
		"""
		Should allow floating point input with multiple digits before and after the decimal mark
		1111.11111 -> 1111.11111
		123.567 -> 123.567
		:return:
		"""
		allure.dynamic.title("Should allow floating point input with multiple "
		                     "digits before and after the decimal mark test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		digit = '1111.11111'
		with allure.step("Enter following digit: {}".format(digit)):
			self.enter_digit(digit)
			self.app.equal.tap()

			with allure.step("Check the result"):
				assert self.app.screen_result.label == '1111.11111'

		digit = '123.567'
		with allure.step("Enter following digit: {}".format(digit)):
			self.enter_digit(digit)
			self.app.equal.tap()

			with allure.step("Check the result"):
				assert self.app.screen_result.label == '123.567'

	def test_allow_a_first_decimal_operand_to_display_a_leading_zero(self):
		"""
		Should allow a first decimal operand to display a leading zero
		0.6 -> 0.6
		.6 -> 0.6
		:return:
		"""
		allure.dynamic.title("Should allow a first decimal operand to display a leading zero test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		with allure.step("Enter following: 0.6 = "):
			self.enter_digit('0.6')
			self.app.equal.tap()

			with allure.step("Check the result"):
				assert self.app.screen_result.label == '0.6'

		with allure.step("Enter following: .6 = "):
			self.enter_digit('.6')
			self.app.equal.tap()

			with allure.step("Check the result"):
				assert self.app.screen_result.label == '0.6'

	def test_allow_the_second_decimal_operand_to_display_a_leading_zero(self):
		"""
		Should allow the second decimal operand to display a leading zero
		6 * 0.6 -> 0.6
		6 * .6 -> 0.6
		:return:
		"""
		allure.dynamic.title("Should allow the second decimal operand to display a leading zero test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		with allure.step("Enter following: 6 * 0.6"):
			self.enter_digit(6)
			self.app.multiplication.tap()
			self.enter_digit('0.6')
			self.app.equal.tap()

			with allure.step("Check the result"):
				assert self.app.screen_result.label == '3.6'

		with allure.step("Enter following: 6 * .6 = "):
			self.enter_digit(6)
			self.app.multiplication.tap()
			self.enter_digit('.6')
			self.app.equal.tap()

			with allure.step("Check the result"):
				assert self.app.screen_result.label == '3.6'

	def test_allow_floating_point_input_with_single_digit_before_and_after_the_decimal_mark(self):
		"""
		Should allow floating point input with a single digit before and after the decimal mark
		1.1 -> 1.1
		:return:
		"""
		allure.dynamic.title("Should allow floating point input with a single "
		                     "digit before and after the decimal mark test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		digit = '1.1'
		with allure.step("Enter following digit: {}".format(digit)):
			self.enter_digit(digit)
			self.app.equal.tap()

			with allure.step("Check the result"):
				assert self.app.screen_result.label == '1.1'

	def test_not_count_a_decimal_mark_against_max_input(self):
		"""
		Should not count a decimal mark against max input
		12.3456789 -> 12.3456789
		:return:
		"""
		allure.dynamic.title("Should not count a decimal mark against max input test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		digit = '12.3456789'
		with allure.step("Enter following digit: {}".format(digit)):
			self.enter_digit(digit)
			self.app.equal.tap()

			with allure.step("Check the result"):
				assert self.app.screen_result.label == '12.3456789'

	def test_not_allow_a_double_negation(self):
		"""
		Should not allow a double negation
		- - 21 =
		:return:
		"""
		allure.dynamic.title("Should not allow a double negation test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		digit = '-21'
		with allure.step("Enter following: -{}".format(digit)):
			self.app.minus.tap()
			self.enter_digit(-21)
			self.app.equal.tap()

			with allure.step("Check the result"):
				assert self.app.screen_result.label == '-21'

	def test_allow_the_maximum_input_when_the_first_digit_is_zero(self):
		"""
		Should allow the maximum input when the first digit is zero
		0123456789 -> 1234567
		:return:
		"""
		allure.dynamic.title("Should allow the maximum input when the first digit is zero test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		digit = '0123456789'
		with allure.step("Input with the first digit as zero : {}".format(digit)):
			self.enter_digit(digit)
			self.app.equal.tap()

			with allure.step("Check the result"):
				assert self.app.screen_result.label == '123456789'
