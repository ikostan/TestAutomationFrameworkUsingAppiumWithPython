"""Open Source License Test"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from tests.calculator_tests.base_testcase import BaseTestCase


@allure.epic('Android Native App')
@allure.parent_suite('Non Functional Test')
@allure.suite("Calculator Test Suite")
@allure.sub_suite("Positive Tests")
@allure.feature("Open Source License")
@allure.story('Open Source Licenses Menu')
class TestOpenSourceLicenseCase(BaseTestCase):
	"""Test that open source license is acceptable and can be displayed"""

	def test_something(self):
		pass
