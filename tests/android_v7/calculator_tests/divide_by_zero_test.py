"""Android Calculator App Test: Divide By Zero Test Case"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import pytest

from tests.android_v7.calculator_tests.calculator_base_testcase import AndroidCalculatorBaseTestCase


@allure.epic('Android Native App')
@allure.parent_suite('Functional Test')
@allure.suite("Calculator Test Suite")
@allure.sub_suite("Negative Tests")
@allure.feature("Division Calculation")
@allure.story('Division By Zero')
class TestDivideByZeroCase(AndroidCalculatorBaseTestCase):
	"""
	Android Calculator App Test: Divide By Zero Test Case
	Should report error for division by 0
	Test the condition where some number divided by zero
	"""

	@pytest.mark.skip("Not implemented")
	def test_report_error_for_division_by_zero(self):
		"""
		Should report error for division by 0
		1500 / 0 = Error
		:return:
		"""
		allure.dynamic.title("Report error for division by 0 test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		#
		numbers = [1500 / 0]
		with allure.step("Check error for division by 0: {}".format(numbers)):
			self.perform_division(numbers)
			pass

