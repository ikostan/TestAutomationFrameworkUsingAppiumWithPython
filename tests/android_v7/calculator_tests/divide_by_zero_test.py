"""Android Calculator App Test: Divide By Zero Test Case"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
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

	Test the condition where some number divided by zero
	"""
	pass

