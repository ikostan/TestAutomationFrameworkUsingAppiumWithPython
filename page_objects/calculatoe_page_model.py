"""Calculator Page Model Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from drivers.element.base_element import BaseElement
from page_locators.calculator_page_locator import CalculatorPageLocator


class CalculatorPageModel:

	def __init__(self, driver):
		self._driver = driver

		# digits
		self._0 = BaseElement(driver=driver, locator=CalculatorPageLocator.DIGITS[0])
		self._1 = BaseElement(driver=driver, locator=CalculatorPageLocator.DIGITS[1])
		self._2 = BaseElement(driver=driver, locator=CalculatorPageLocator.DIGITS[2])
		self._3 = BaseElement(driver=driver, locator=CalculatorPageLocator.DIGITS[3])
		self._4 = BaseElement(driver=driver, locator=CalculatorPageLocator.DIGITS[4])
		self._5 = BaseElement(driver=driver, locator=CalculatorPageLocator.DIGITS[5])
		self._6 = BaseElement(driver=driver, locator=CalculatorPageLocator.DIGITS[6])
		self._7 = BaseElement(driver=driver, locator=CalculatorPageLocator.DIGITS[7])
		self._8 = BaseElement(driver=driver, locator=CalculatorPageLocator.DIGITS[8])
		self._9 = BaseElement(driver=driver, locator=CalculatorPageLocator.DIGITS[9])

		self._digits = [self._0, self._1, self._2, self._3, self._4,
		                self._5, self._6, self._7, self._8, self._9]

		self._minus = BaseElement(driver=driver, locator=CalculatorPageLocator.MINUS_BTN)
		self._plus = BaseElement(driver=driver, locator=CalculatorPageLocator.PLUS_BTN)
		self._multiplication = BaseElement(driver=driver, locator=CalculatorPageLocator.MULTIPLICATION_BTN)
		self._division = BaseElement(driver=driver, locator=CalculatorPageLocator.DIVISION_BTN)
		self._equal = BaseElement(driver=driver, locator=CalculatorPageLocator.EQUAL_BTN)
		self._minus = BaseElement(driver=driver, locator=CalculatorPageLocator.MINUS_BTN)
		self._dot = BaseElement(driver=driver, locator=CalculatorPageLocator.POINT_BTN)

		self._buttons = [self._0, self._1, self._2, self._3, self._4,
		                 self._5, self._6, self._7, self._8, self._9,
		                 self._minus, self._plus, self._multiplication,
		                 self._division, self._equal, self._minus, self._dot]

		self._main_screen = BaseElement(driver=driver, locator=CalculatorPageLocator.DISPLAY)

		# self._del = None
		# self._clr = None
		# self._screen_formula = None
		# self._screen_result = None

	@property
	def screen_formula(self):
		return BaseElement(driver=self.driver, locator=CalculatorPageLocator.SCREEN_FORMULA)

	@property
	def screen_result(self):
		return BaseElement(driver=self.driver, locator=CalculatorPageLocator.SCREEN_RESULT)

	@property
	def clr(self):
		return BaseElement(driver=self.driver, locator=CalculatorPageLocator.CLEAR_BTN)

	@property
	def del_btn(self):
		return BaseElement(driver=self.driver, locator=CalculatorPageLocator.DEL_BTN)

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

	'''
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

	def is_element_visible(self, locator):
		"""
		Returns element visibility
		:param locator: 
		:return: 
		"""
		return BaseElement(self.driver, locator).is_visible
	'''
