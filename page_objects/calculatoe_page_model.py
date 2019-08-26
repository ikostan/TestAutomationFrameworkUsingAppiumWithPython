"""Calculator Page Model Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from drivers.element.base_element import BaseElement
from page_locators.calculator_page_locator import CalculatorPageLocator


class CalculatorPageModel:

	def __init__(self, driver):
		self._driver = driver

	@property
	def driver(self):
		"""
		Returns driver object
		:return:
		"""
		return self._driver

	def tap_digit(self, digit):
		"""
		Tap on digit.
		Digits allowed: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
		:param digit:
		:return:
		"""
		digit = BaseElement(driver=self.driver, locator=CalculatorPageLocator.DIGITS[digit])
		digit.tap()
		return None



