"""Open Source License Test"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
from tests.calculator_tests.calculator_base_testcase import AndroidCalculatorBaseTestCase


@allure.epic('Android Native App')
@allure.parent_suite('Non Functional Test')
@allure.suite("Calculator Test Suite")
@allure.sub_suite("Positive Tests")
@allure.feature("Open Source License")
@allure.story('Open Source Licenses Menu')
class TestOpenSourceLicenseCase(AndroidCalculatorBaseTestCase):
	"""Test that open source license is acceptable and can be displayed"""
	pass
