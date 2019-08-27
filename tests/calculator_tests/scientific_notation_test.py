"""Scientific Notation Conversion"""
#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from tests.calculator_tests.base_testcase import BaseTestCase


@allure.epic('Android Native App')
@allure.parent_suite('Functional Test')
@allure.suite("Calculator Test Suite")
@allure.sub_suite("Positive Tests")
@allure.feature("Scientific Notation")
@allure.story('Scientific Notation Conversion')
class TestScientificNotationConversionCase(BaseTestCase):

	def test_something(self):
		pass


if __name__ == '__main__':
	unittest.main()
