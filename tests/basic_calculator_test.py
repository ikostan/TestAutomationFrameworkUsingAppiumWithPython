#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import unittest
import allure

from utils.driver import Driver
from utils.screenshot import screenshot_on_fail

from locators.page_locator import PageLocator

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic('Android Built-In App')
@allure.parent_suite('End To End')
@allure.suite("Calculator Test Suite")
@allure.sub_suite("Positive Tests")
@allure.feature("Basic Functionality")
@allure.story('Basic Buttons')
@screenshot_on_fail()
class TestBasicCalculatorCases(unittest.TestCase):
	"""
	Test basic functionality:

	Should be able to open Calculator app
	Should be able to enter digits
	Should be able to use "=" button
	Should be able to use "DEL" button
	Should be able to use "CLR" button
	Should be able to see input/output
	Should be able to close the app
	"""

	def setUp(self) -> None:
		self.driver = Driver()
		self.driver.instance.implicitly_wait(3)

	def tearDown(self) -> None:
		if self.driver.instance:
			self.driver.instance.quit()
			self.driver = None

	def test_entering_digits(self):
		"""
		Should be able to open Calculator app
		Should be able to enter digits
		Should be able to see input/output
		Should be able to close the app
		:return:
		"""

		for key in PageLocator.DIGITS.keys():
			btn = WebDriverWait(self.driver.instance, 5).until(EC.element_to_be_clickable(PageLocator.DIGITS[key]))
			btn.click()

		screen_formula = WebDriverWait(self.driver.instance, 5).until(
			EC.presence_of_element_located(PageLocator.SCREEN_FORMULA))
		assert '0123456789' == screen_formula.text

	def test_equal_btn(self):
		"""
		Should be able to open Calculator app
		Should be able to enter digits
		Should be able to use "=" button
		Should be able to see input/output
		Should be able to close the app
		:return:
		"""

		for key in PageLocator.DIGITS.keys():
			btn = WebDriverWait(self.driver.instance, 5).until(EC.element_to_be_clickable(PageLocator.DIGITS[key]))
			btn.click()

		btn = WebDriverWait(self.driver.instance, 5).until(
			EC.element_to_be_clickable(PageLocator.EQUAL_BTN))
		btn.click()

		screen_result = WebDriverWait(self.driver.instance, 5).until(
			EC.presence_of_element_located(PageLocator.SCREEN_RESULT))
		assert '123456789' == screen_result.text

	def test_clear_btn(self):
		"""
		Should be able to open Calculator app
		Should be able to use "CLR" button
		Should be able to close the app
		:return:
		"""

		for key in PageLocator.DIGITS.keys():
			btn = WebDriverWait(self.driver.instance, 5).until(EC.element_to_be_clickable(PageLocator.DIGITS[key]))
			btn.click()

		btn = WebDriverWait(self.driver.instance, 5).until(
			EC.element_to_be_clickable(PageLocator.EQUAL_BTN))
		btn.click()

		btn = WebDriverWait(self.driver.instance, 5).until(EC.element_to_be_clickable(PageLocator.CLEAR_BTN))
		btn.click()

		screen_formula = WebDriverWait(self.driver.instance, 5).until(
			EC.presence_of_element_located(PageLocator.SCREEN_FORMULA))
		assert '' == screen_formula.text

		screen_result = WebDriverWait(self.driver.instance, 5).until(
			EC.presence_of_element_located(PageLocator.SCREEN_RESULT))
		assert '' == screen_result.text

	def test_delete_btn(self):
		"""
		Should be able to open Calculator app
		Should be able to enter digits
		Should be able to use "DEL" button
		Should be able to see input/output
		Should be able to close the app
		:return:
		"""

		for key in PageLocator.DIGITS.keys():
			btn = WebDriverWait(self.driver.instance, 5).until(EC.element_to_be_clickable(PageLocator.DIGITS[key]))
			btn.click()

		for n in range(len('0123456789')):

			btn = WebDriverWait(self.driver.instance, 5).until(
				EC.element_to_be_clickable(PageLocator.DEL_BTN))
			btn.click()

			screen_formula = WebDriverWait(self.driver.instance, 5).until(
				EC.presence_of_element_located(PageLocator.SCREEN_FORMULA))
			assert '0123456789'[0:len('0123456789') - (1 + n)] == screen_formula.text

		screen_formula = WebDriverWait(self.driver.instance, 5).until(
			EC.presence_of_element_located(PageLocator.SCREEN_FORMULA))
		assert '' == screen_formula.text

		screen_result = WebDriverWait(self.driver.instance, 5).until(
			EC.presence_of_element_located(PageLocator.SCREEN_RESULT))
		assert '' == screen_result.text




