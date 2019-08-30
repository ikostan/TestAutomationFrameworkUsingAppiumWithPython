"""License Page Model Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_locators.license_page_locator import LicensePageLocator


class LicensePageModel:
	"""
	License Page Model Class
	"""

	def __init__(self, driver):
		self._driver = driver

		print("Waiting for License view...")
		WebDriverWait(self._driver, 5).until(
			EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/'
			                                          'android.view.ViewGroup/android.widget.FrameLayout[1]/'
			                                          'android.view.ViewGroup/android.widget.TextView')))
		print("License view is opened...")

	@property
	def driver(self):
		"""
		Returns driver object
		:return:
		"""
		return self._driver

	def _get_txt(self, locator: tuple):
		"""
		1. Switch to web view
		2. Extract text
		3. Switch to Native view
		4. Returns text
		:return:
		"""
		self.driver.switch_to.context("WEBVIEW_com.android.calculator2")
		print('Context switched to web view')

		txt = self.driver.find_element(by=locator[0],
		                               value=locator[1]).text

		self.driver.switch_to.context('NATIVE_APP')
		print('Context switched to native view')

		return txt

	@property
	def header(self):
		"""
		1. Switch to web view
		2. Extract text
		3. Switch to Native view
		4. Returns h3 header
		:return:
		"""
		txt = self._get_txt(LicensePageLocator.HEADER)
		print("Extracting Open Source License header")
		return txt

	@property
	def crc(self):
		"""
		1. Switch to web view
		2. Extract text
		3. Switch to Native view
		4. Returns CRC header
		:return:
		"""
		crc = self._get_txt(LicensePageLocator.CRC)
		print("Extracting Open Source License CRC")
		return crc

	@property
	def full_license_txt(self):
		"""
		1. Switch to web view
		2. Extract text
		3. Switch to Native view
		4. Returns Licence text
		:return:
		"""
		txt = self._get_txt(LicensePageLocator.FULL_TEXT)
		print("Extracting full Open Source License text")
		return txt

	@property
	def title(self):
		"""
		Extracts title from native view
		:return:
		"""
		txt = self.driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/'
		                                               'android.view.ViewGroup/android.widget.FrameLayout[1]/'
		                                               'android.view.ViewGroup/android.widget.TextView').text
		print("Extracting Open Source License title")
		return txt

	@property
	def arrow_btn(self):
		"""
		Returns Arrow Button object
		:return:
		"""
		print("Extracting Arrow button from Open Source License view")
		return self.driver.find_element(by=LicensePageLocator.ARROW_BTN[0],
		                                value=LicensePageLocator.ARROW_BTN[1])
