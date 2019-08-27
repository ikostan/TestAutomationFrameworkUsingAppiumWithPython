"""Divide By Zero Test Case"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
from tests.calculator_tests.base_testcase import BaseTestCase


@allure.epic('Android Native App')
@allure.parent_suite('Functional Test')
@allure.suite("Calculator Test Suite")
@allure.sub_suite("Negative Tests")
@allure.feature("Division Calculation")
@allure.story('Division Button')
class TestDivideByZeroCase(BaseTestCase):
	"""
	Test the condition where some number divided by zero
	"""

	def test_something(self):
		pass
