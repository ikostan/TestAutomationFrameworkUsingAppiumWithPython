"""Android Calculator App Test: Multi Touch Test Case"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
from tests.calculator_tests.calculator_base_testcase import AndroidCalculatorBaseTestCase


@allure.epic('Android Native App')
@allure.parent_suite('Non Functional Test')
@allure.suite("Calculator Test Suite")
@allure.sub_suite("Positive Tests")
@allure.feature("Multi Touch Functionality")
@allure.story('Multi Touch Support')
class TestMultiTouchCase(AndroidCalculatorBaseTestCase):
	"""
	Android Calculator App Test: Multi Touch Test Case

	Perform tests with a multi touch action sequence

	Documentation:

	An Overview of the TouchAction / MultiAction API:
	http://appium.io/docs/en/writing-running-appium/touch-actions/

	Multi Touch Perform:
	http://appium.io/docs/en/commands/interactions/touch/multi-touch-perform/

	multi_action.py:
	https://github.com/appium/python-client/blob/master/appium/webdriver/common/multi_action.py

	touch_action.py:
	https://github.com/appium/python-client/blob/master/appium/webdriver/common/touch_action.py
	"""
	pass

