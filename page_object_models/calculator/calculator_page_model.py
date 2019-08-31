"""Calculator Page Model Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/
from appium.webdriver.common.touch_action import TouchAction

from page_object_models.calculator.element.base_element_model import BaseElementModel
from page_locators.calculator_page_locator import CalculatorPageLocator
from selenium.common.exceptions import TimeoutException

from page_object_models.calculator.license_page_model import LicensePageModel


class CalculatorPageModel:

	def __init__(self, driver):
		self._driver = driver

		# digits
		self._0 = BaseElementModel(driver=driver, locator=CalculatorPageLocator.DIGITS[0])
		self._1 = BaseElementModel(driver=driver, locator=CalculatorPageLocator.DIGITS[1])
		self._2 = BaseElementModel(driver=driver, locator=CalculatorPageLocator.DIGITS[2])
		self._3 = BaseElementModel(driver=driver, locator=CalculatorPageLocator.DIGITS[3])
		self._4 = BaseElementModel(driver=driver, locator=CalculatorPageLocator.DIGITS[4])
		self._5 = BaseElementModel(driver=driver, locator=CalculatorPageLocator.DIGITS[5])
		self._6 = BaseElementModel(driver=driver, locator=CalculatorPageLocator.DIGITS[6])
		self._7 = BaseElementModel(driver=driver, locator=CalculatorPageLocator.DIGITS[7])
		self._8 = BaseElementModel(driver=driver, locator=CalculatorPageLocator.DIGITS[8])
		self._9 = BaseElementModel(driver=driver, locator=CalculatorPageLocator.DIGITS[9])

		self._digits = {0: self._0,
		                1: self._1,
		                2: self._2,
		                3: self._3,
		                4: self._4,
		                5: self._5,
		                6: self._6,
		                7: self._7,
		                8: self._8,
		                9: self._9}

		# Buttons
		self._minus = BaseElementModel(driver=driver, locator=CalculatorPageLocator.MINUS_BTN)
		self._plus = BaseElementModel(driver=driver, locator=CalculatorPageLocator.PLUS_BTN)
		self._multiplication = BaseElementModel(driver=driver, locator=CalculatorPageLocator.MULTIPLICATION_BTN)
		self._division = BaseElementModel(driver=driver, locator=CalculatorPageLocator.DIVISION_BTN)
		self._equal = BaseElementModel(driver=driver, locator=CalculatorPageLocator.EQUAL_BTN)
		self._minus = BaseElementModel(driver=driver, locator=CalculatorPageLocator.MINUS_BTN)
		self._dot = BaseElementModel(driver=driver, locator=CalculatorPageLocator.POINT_BTN)

		# All butt5ons
		self._buttons = [self._0, self._1, self._2, self._3, self._4,
		                 self._5, self._6, self._7, self._8, self._9,
		                 self._minus, self._plus, self._multiplication,
		                 self._division, self._equal, self._minus, self._dot]

		# Screens
		self._main_screen = BaseElementModel(driver=driver, locator=CalculatorPageLocator.DISPLAY)

		# More Options menu
		self._more_options = BaseElementModel(driver=driver, locator=CalculatorPageLocator.MORE_OPTIONS)

	def open_license(self):
		"""
		1. Tap More Options menu
		2. Tap on "More Options"
		3. Returns "LicensePageModel" object
		:return:
		"""

		TouchAction(self._driver).tap(self._more_options.element).wait(3).perform()
		print('Tap on "More Options"')
		open_source_license = BaseElementModel(driver=self._driver, locator=CalculatorPageLocator.OPEN_SOURCE_LICENSE)
		TouchAction(self._driver).tap(open_source_license.element).wait(3).perform()
		print('Tap on "Open Source License"')
		return LicensePageModel(self._driver)

	@property
	def screen_formula(self):
		try:
			return BaseElementModel(driver=self.driver, locator=CalculatorPageLocator.SCREEN_FORMULA)
		except TimeoutException:
			return None

	@property
	def screen_result(self):
		try:
			return BaseElementModel(driver=self.driver, locator=CalculatorPageLocator.SCREEN_RESULT)
		except TimeoutException:
			return None

	@property
	def clr(self):
		return BaseElementModel(driver=self.driver, locator=CalculatorPageLocator.CLEAR_BTN)

	@property
	def del_btn(self):
		return BaseElementModel(driver=self.driver, locator=CalculatorPageLocator.DEL_BTN)

	@property
	def buttons(self):
		return self._buttons

	@property
	def digits(self):
		return self._digits

	@property
	def dot(self):
		return self._dot

	@property
	def division(self):
		return self._division

	@property
	def multiplication(self):
		return self._multiplication

	@property
	def equal(self):
		return self._equal

	@property
	def plus(self):
		return self._plus

	@property
	def minus(self):
		return self._minus

	@property
	def zero(self):
		return self._0

	@property
	def one(self):
		return self._1

	@property
	def two(self):
		return self._2

	@property
	def tree(self):
		return self._3

	@property
	def four(self):
		return self._4

	@property
	def five(self):
		return self._5

	@property
	def six(self):
		return self._6

	@property
	def seven(self):
		return self._7

	@property
	def eight(self):
		return self._8

	@property
	def nine(self):
		return self._9

	@property
	def main_screen(self):
		return self._main_screen

	@property
	def driver(self):
		"""
		Returns driver object
		:return:
		"""
		return self._driver

