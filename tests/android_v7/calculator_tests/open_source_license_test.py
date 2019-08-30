"""Android Calculator App Test: Open Source License Test"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure

from appium.webdriver.common.touch_action import TouchAction

from tests.android_v7.calculator_tests.calculator_base_testcase import AndroidCalculatorBaseTestCase


@allure.epic('Android Native App')
@allure.parent_suite('Non Functional Test')
@allure.suite("Calculator Test Suite")
@allure.sub_suite("Positive Tests")
@allure.feature("Open Source License")
@allure.story('Open Source Licenses Menu')
class TestOpenSourceLicenseCase(AndroidCalculatorBaseTestCase):
	"""
	Android Calculator App Test: Open Source License Test
	Test that open source license is acceptable and can be displayed
	"""

	def test_open_source_license(self):
		"""
		1. Open Calculator App
		2. Open "Open Source License" page/view
		3. Verify Title
		4. Close it and go back to calculator
		5. Close calculator app
		:return:
		"""

		self.app = self.app.open_license()

		assert self.app.header == 'Notices for files:'

		assert self.app.crc == 'CRCalc'

		assert self.app.full_license_txt == self.sample_license_txt

		assert self.app.title == 'Open source licenses'

		TouchAction(self.app.driver).tap(self.app.arrow_btn).wait(5).perform()

	@property
	def sample_license_txt(self) -> str:
		"""
		Returns license text from stored/source file
		:return:
		"""

		license_file_name = 'C:/Users/superadmin/Documents/GitHub/' \
		                    'TEST_AUTOMATION_FRAMEWORK_USING_APPIUM_WITH_PYTHON/' \
		                    'files/open_source_license.txt'
		license_txt = ''

		with open(license_file_name, "r", encoding="utf-8") as f:
			for line in f:
				license_txt += line

		return license_txt
