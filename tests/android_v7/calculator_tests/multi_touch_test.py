"""Android Calculator App Test: Multi Touch Test Case"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure

from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction

from tests.android_v7.calculator_tests.calculator_base_testcase import AndroidCalculatorBaseTestCase


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

	def test_multi_touch_action(self):
		"""
		Test multi touch action
		:return:
		"""

		allure.dynamic.title("Multi touch action test")
		allure.dynamic.severity(allure.severity_level.MINORL)

		with allure.step("Enter following using multi touch action: 12"):
			touch_action_1 = TouchAction().tap(self.app.digits[1])
			touch_action_2 = TouchAction().tap(self.app.digits[2])

			multi_touch_action = MultiAction(self.app.driver)
			multi_touch_action.add(touch_action_2, touch_action_1)
			multi_touch_action.perform()

			with allure.step("Verify screen output"):
				assert self.app.screen_formula.label == '12'


