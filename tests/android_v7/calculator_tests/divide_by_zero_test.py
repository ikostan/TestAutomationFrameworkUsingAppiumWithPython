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
@allure.feature("Invalid Scenarios")
@allure.story('Division By Zero')
class TestDivideByZeroCase(AndroidCalculatorBaseTestCase):
	"""
	Android Calculator App Test: Divide By Zero Test Case
	Should report error for division by 0
	Test the condition where some number divided by zero
	"""

	def test_report_error_for_division_by_zero(self):
		"""
		Should report error for division by 0
		1500 / 0 = Error
		:return:
		"""
		allure.dynamic.title("Report error for division by 0 test")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		# Perform division by zero
		with allure.step("Check error for division by 0: 1500 / 0 -> ERROR"):
			self.enter_digit(1500)
			self.app.division.tap()
			self.enter_digit(0)
			self.app.equal.tap()

			with allure.step("Verify error message"):
				expected = 'Can\'t divide by 0'
				assert self.app.screen_result.label == expected

