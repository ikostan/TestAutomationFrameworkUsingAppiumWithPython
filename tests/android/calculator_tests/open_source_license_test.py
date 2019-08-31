"""Android Calculator App Test: Open Source License Test"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure

from tests.android.calculator_tests.calculator_base_testcase import AndroidCalculatorBaseTestCase


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
		3. Verify Title, CRC, Header, full license text
		4. Go back to calculator
		5. Verify that some of the calculator buttons are visible (0-9)
		6. Test basic buttons functionality
		7. Close calculator app
		:return:
		"""

		allure.dynamic.title("Open Source License View Test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step("Go to Open Source License view"):
			self.app = self.app.open_license()

		with allure.step("Verify Open Source License header"):
			assert self.app.header == 'Notices for files:'

		with allure.step("Verify Open Source License CRCalc"):
			assert self.app.crc == 'CRCalc'

		with allure.step("Verify Open Source License full text"):
			assert self.app.full_license_txt == self.sample_license_txt

		with allure.step("Verify Open Source License title"):
			assert self.app.title == 'Open source licenses'

		with allure.step("Go back to Calculator view"):
			self.app = self.app.tap_arrow_btn()

		# Digits 0-9
		with allure.step("Test 0-9 digits/buttons visibility"):
			for btn in self.app.buttons:
				assert btn.is_visible

		with allure.step("Test basic buttons functionality"):
			with allure.step("Enter digits 0-9"):
				self.enter_digit("0123456789")

			with allure.step("Press '=' button"):
				self.app.equal.tap()

			with allure.step("Verify screen output"):
				assert self.app.screen_result.formatted_text == '123456789'

	@property
	def sample_license_txt(self) -> str:
		"""
		Returns license text from stored/source file
		:return:
		"""

		with allure.step("Extract Source License full text sample from source file"):

			license_file_name = 'C:/Users/superadmin/Documents/' \
			                    'GitHub/TEST_AUTOMATION_FRAMEWORK_USING_APPIUM_WITH_PYTHON/' \
			                    'tests/android/calculator_tests/open_source_license.txt'
			license_txt = ''

			with open(license_file_name, "r", encoding="utf-8") as f:
				for line in f:
					license_txt += line

			return license_txt
