"""Android Calculator App Test: Subtraction Test Case"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
from tests.android_v7_calculator_tests.calculator_base_testcase import AndroidCalculatorBaseTestCase


@allure.epic('Android Native App')
@allure.parent_suite('Functional Test')
@allure.suite("Calculator Test Suite")
@allure.sub_suite("Positive Tests")
@allure.feature("Subtraction Calculation")
@allure.story('Subtraction Button')
class TestSubtractionCase(AndroidCalculatorBaseTestCase):
	"""
	Android Calculator App Test: Subtraction Test Case

    Terminology:
    Minuend - Subtrahend = Difference

    Should be able to subtract two positive integers
    Should be able to subtract zero from a negative integer
    Should be able to subtract 0 from a positive integer
    Should be able to subtract a floating point number from a negative integer
    Should be able to subtract an integer from the results of a previous operation
    Should be able to subtract an integer from a floating point number
    Should be able to subtract a floating point number from an integer
    Should be able to subtract two floating point numbers
    Should be able to subtract two max-input floating point numbers
    An addition of a negative floating point addend, to an integer addend should be treated
    as a subtraction of a positive integer subtrahend

    An addition of a negative floating point addend should be treated as a subtraction
    of a positive floating point subtrahend

    An addition of a negative integer addend should be treated as a subtraction
    of a poisitive integer subtrahend

    An addition of a negative integer addend to another negative integer addend should be treated
    as a subtraction of a poisitive integer subtrahend

    Should be able to subtract a floating point number from the result of a previous operation
    Should be able to subtract an integer from a negative floating point number
    Should be able to subtract two large integers
    Should be able to subtract two floating point numbers with many digits
    Should be able to subtract a large decimal number from the results of a previous result
    Should be able to subtract a large integer from the results of a previous result

    Source: http://mozilla.github.io/calculator/test/
    """

	def test_subtract_two_positive_integers(self):
		"""
        User should be able to subtract two positive integers:
        1500 - 2000 = -500
        :return:
        """
		allure.dynamic.title("Subtraction of two positive integers test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1500 - 2000 = -500
		numbers = [1500, 2000]
		with allure.step("Test subtraction of two positive integers: {}".format(numbers)):
			self.perform_subtraction(numbers)
			assert self.app.screen_result.label == self.eval_formula(1500 - 2000)

	def test_subtract_zero_from_a_negative_integer(self):
		"""
        Should be able to subtract zero from a negative integer:
        -3 - 0 = -3
        :return:
        """
		allure.dynamic.title("Subtraction of zero from a negative integer test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# -3 - 0 = -3
		numbers = [-3, 0]
		with allure.step("Test subtraction of zero from a negative integer: {}".format(numbers)):
			self.perform_subtraction(numbers)
			assert self.app.screen_result.label == self.eval_formula(-3 - 0)

	def test_subtract_0_from_a_positive_integer(self):
		"""
        Should be able to subtract 0 from a positive integer:
        3 - 0 = 3
        :return:
        """
		allure.dynamic.title("Subtraction of 0 from a positive integer test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 3 - 0 = 3
		numbers = [3, 0]
		with allure.step("Test subtraction of 0 from a positive integer: {}".format(numbers)):
			self.perform_subtraction(numbers)
			assert self.app.screen_result.label == self.eval_formula(3 - 0)

	def test_subtract_a_floating_point_number_from_a_negative_integer(self):
		"""
        Should be able to subtract a floating point number from a negative integer:
        -1 - 2.25 = -3.25
        :return:
        """
		allure.dynamic.title("Subtraction of floating point number from a negative integer test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# -1 - 2.25 = -3.25
		numbers = [-1, 2.25]
		with allure.step("Test subtraction of floating point number from a negative integer: {}".format(numbers)):
			self.perform_subtraction(numbers)
			assert self.app.screen_result.label == self.eval_formula(-1 - 2.25)

	def test_subtract_an_integer_from_the_results_of_a_previous_operation(self):
		"""
        Should be able to subtract an integer from the results of a previous operation:
        1500 - 2000 = -500 - 500 =
        6 * 2 = 12 - 8 = 4
        :return:
        """
		allure.dynamic.title("Subtraction of integer from the results of a previous operation test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1500 - 2000 = -500 - 500 =
		numbers = [1500, 2000, -500, 500]
		with allure.step("Test subtraction of integer from the results of a previous operation: {}".format(numbers)):
			self.perform_subtraction(numbers)
			assert self.app.screen_result.label == self.eval_formula(1500 - 2000 - 500 - 500)

		numbers = [6, 2, 12, 8]
		with allure.step("Test subtraction of integer from the results of a previous operation: {}".format(numbers)):
			self.enter_number(6)
			self.app.multiplication.tap()
			self.enter_number(2)
			self.app.equal.tap()
			self.enter_number(12)
			self.app.minus.tap()
			self.enter_number(8)
			self.app.equal.tap()
			assert self.app.screen_result.label == self.eval_formula(12 - 8)

	def test_subtract_an_integer_from_a_floating_point_number(self):
		"""
        Should be able to subtract an integer from a floating point number:
        9.35 - 1 = 8.35
        :return:
        """
		allure.dynamic.title("Subtraction of an integer from a floating point number test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 9.35 - 1 = 8.35
		numbers = [9.35, 1]
		with allure.step("Test subtraction of of an integer from a floating point number: {}".format(numbers)):
			self.perform_subtraction(numbers)
			assert self.app.screen_result.label == self.eval_formula(9.35 - 1)

	def test_subtract_a_floating_point_number_from_an_integer(self):
		"""
        Should be able to subtract a floating point number from an integer:
        9 - 1.35 = 7.65
        :return:
        """
		allure.dynamic.title("Subtraction a floating point number from an integer test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 9 - 1.35 = 7.65
		numbers = [9, 1.35]
		with allure.step("Test subtraction a floating point number from an integers: {}".format(numbers)):
			self.perform_subtraction(numbers)
			assert self.app.screen_result.label == self.eval_formula(9 - 1.35)

	def test_subtract_two_floating_point_numbers(self):
		"""
        Should be able to subtract two max-input floating point numbers:
        0.29 - 1.35 = -1.06
        :return:
        """
		allure.dynamic.title("Subtraction of two max-input floating point numbers test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 0.29 - 1.35 = -1.06
		numbers = [0.29, 1.35]
		with allure.step("Test subtraction of two max-input floating point numbers: {}".format(numbers)):
			self.perform_subtraction(numbers)
			assert self.app.screen_result.label == self.eval_formula(0.29 - 1.35)

	def test_subtract_two_max_input_floating_point_numbers(self):
		"""
        Should be able to subtract two max-input floating point numbers:
        7.1234567 - 2.2109876 = 4.9124691
        :return:
        """
		allure.dynamic.title("Subtraction of two max-input floating point numbers")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 7.1234567 - 2.2109876 = 4.9124691
		numbers = [7.1234567, 2.2109876]
		with allure.step("Test subtraction of two max-input floating point numbers: {}".format(numbers)):
			self.enter_number(7.1234567)
			self.app.minus.tap()
			self.enter_number(2.2109876)
			self.app.equal.tap()
			assert self.app.screen_result.label == self.eval_formula(7.1234567 - 2.2109876)

	def test_addition_of_a_negative_floating_point_addend_to_an_integer_addend(self):
		"""
        An addition of a negative floating point addend should be treated as a
        subtraction of a positive floating point subtrahend:
        # 1000 + - 10.99 = 989.01
        :return:
        """
		allure.dynamic.title("Subtraction of positive floating point subtrahend test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1000 + - 10.99 = 989.01
		numbers = [1000, -10.99]
		with allure.step("Test subtraction of positive floating point subtrahend: {}".format(numbers)):
			self.enter_number(1000)
			self.app.plus.tap()
			self.enter_number(-10.99)
			self.app.equal.tap()
			assert self.app.screen_result.label == self.eval_formula(1000 + (-10.99))

	def test_addition_of_a_negative_floating_point_addend(self):
		"""
        An addition of a negative integer addend should be treated
        as a subtraction of a poisitive integer subtrahend:
        1.0 + - 989.99
        :return:
        """
		allure.dynamic.title("Subtraction of a positive integer subtrahend test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1.0 + - 989.99
		numbers = [1.0, -989.9]
		with allure.step("Test subtraction of a positive integer subtrahend: {}".format(numbers)):
			self.enter_number(1.0)
			self.app.plus.tap()
			self.enter_number(-989.99)
			self.app.equal.tap()
			assert self.app.screen_result.label == self.eval_formula(1.0 + (-989.99))

	def test_addition_of_a_negative_integer_addend(self):
		"""
        An addition of a negative integer addend to another negative integer
        addend should be treated as a subtraction of a poisitive integer subtrahend:
        50 + - 60 = -10
        :return:
        """
		allure.dynamic.title("Subtraction of positive integer subtrahend test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 50 + - 60 = -10
		numbers = [50, -60]
		with allure.step("Test subtraction of positive integer subtrahend: {}".format(numbers)):
			self.enter_number(50)
			self.app.plus.tap()
			self.enter_number(-60)
			self.app.equal.tap()
			assert self.app.screen_result.label == self.eval_formula(50 + (-60))

	def test_addition_of_a_negative_integer_addend_to_another_negative_integer_addend(self):
		"""
        Should be able to subtract a floating point number from the result of a previous operation
        -5 + - 20 = -25
        :return:
        """
		allure.dynamic.title("Subtraction of a floating point number from the result of a previous operation test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# -5 + - 20 = -25
		numbers = [-5, -20]
		with allure.step(
				"Test subtraction of a floating point number from the result of a previous operation: {}".format(
					numbers)):
			self.enter_number(-5)
			self.app.plus.tap()
			self.enter_number(-20)
			self.app.equal.tap()
			assert self.app.screen_result.label == self.eval_formula(-5 + (-20))

	def test_subtract_a_floating_point_number_from_the_result_of_a_previous_operation(self):
		"""
        Should be able to subtract an integer from a negative floating point number:
        1500 - 2000 = -500 - 33.12 = -533.12
        :return:
        """
		allure.dynamic.title("Subtraction an integer from a negative floating point number test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1500 - 2000 = -500 - 33.12 =
		numbers = [-1.33, 2]
		with allure.step("Test subtraction of an integer from a negative floating point number: {}".format(numbers)):
			self.enter_number(1500)
			self.app.minus.tap()
			self.enter_number(2000)
			self.app.equal.tap()
			self.enter_number(-500)
			self.app.minus.tap()
			self.enter_number(33.12)
			self.app.equal.tap()
			assert self.app.screen_result.label == self.eval_formula(1500 - 2000 + (-500) - 33.12)

	def test_subtract_an_integer_from_a_negative_floating_point_number(self):
		"""
        Should be able to subtract an integer from a negative floating point number:
        -1.33 - 2 = -3.33
        :return:
        """
		allure.dynamic.title("Subtraction of an integer from a negative floating point number")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# -1.33 - 2 = -3.33
		numbers = [-1.33, 2]
		with allure.step("Test subtraction of an integer from a negative floating point number: {}".format(numbers)):
			self.perform_subtraction(numbers)
			assert self.app.screen_result.label == self.eval_formula(-1.33 - 2)

	def test_subtract_two_large_integers(self):
		"""
        Should be able to subtract two large integers:
        123456789 - 210987654 = -87530865
        :return:
        """
		allure.dynamic.title("Subtraction of two large integers")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 123456789 - 210987654 = -87530865
		numbers = [123456789, 210987654]
		with allure.step("Test subtraction of two large integers: {}".format(numbers)):
			self.perform_subtraction(numbers)
			assert self.app.screen_result.label == self.eval_formula(123456789 - 210987654)

	def test_subtract_two_floating_point_numbers_with_many_digits(self):
		"""
        Should be able to subtract two floating point numbers with many digits:
        # 7.12345678 - 2.21098765 = 4.91246913
        :return:
        """
		allure.dynamic.title("Subtraction of two floating point numbers with many digits")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 7.12345678 - 2.21098765 = 4.91246913
		numbers = [7.12345678, 2.21098765]
		with allure.step("Test subtraction of two floating point numbers with many digits: {}".format(numbers)):
			self.perform_subtraction(numbers)
			assert self.app.screen_result.label == self.eval_formula(7.12345678 - 2.21098765)

	def test_subtract_a_large_decimal_number_from_the_results_of_a_previous_result(self):
		"""
        Should be able to subtract a large decimal number from the results of a previous result:
        1500 - 2000 = -500 - 12.3456789 = -512.3456789
        :return:
        """
		allure.dynamic.title("Subtraction of a large decimal number from the results of a previous result test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1500 - 2000 = -500 - 12.3456789 = -512.3456789
		numbers = [1500, 2000, -500, 12.3456789]
		with allure.step(
				"Test subtraction of a large decimal number from the results of a previous result: {}".format(numbers)):
			self.enter_number(1500)
			self.app.minus.tap()
			self.enter_number(2000)
			self.app.equal.tap()
			self.enter_number(-500)
			self.app.minus.tap()
			self.enter_number(12.3456789)
			self.app.equal.tap()
			assert self.app.screen_result.label == self.eval_formula(1500 - 2000 + (-500) - 12.3456789)

	def test_subtract_a_large_integer_from_the_results_of_a_previous_result(self):
		"""
        Should be able to subtract a large integer from the results of a previous result:
        1500 - 2000 = -500 - 123456789 = -123457289
        :return:
        """
		allure.dynamic.title("Subtraction a large integer from the results of a previous result test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# 1500 - 2000 = -500 - 123456789 = -123457289
		numbers = [1500, 2000, -500, 123456789]
		with allure.step(
				"Test subtraction of a large integer from the results of a previous result: {}".format(numbers)):
			self.enter_number(1500)
			self.app.minus.tap()
			self.enter_number(2000)
			self.app.equal.tap()
			self.enter_number(-500)
			self.app.minus.tap()
			self.enter_number(123456789)
			self.app.equal.tap()
			assert self.app.screen_result.label == self.eval_formula(1500 - 2000 + (-500) - 123456789)
