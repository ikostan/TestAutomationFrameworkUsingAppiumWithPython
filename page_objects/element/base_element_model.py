"""Base Element Definition"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchAttributeException


class BaseElementModel:

	def __init__(self, driver, locator: tuple):
		self._driver = driver
		self._locator = locator
		self._element = self._set_element()

	@property
	def id(self):
		"""
		Returns element id
		:return:
		"""
		return self._element.id

	def _set_element(self):
		return WebDriverWait(self._driver, 5).until(
			EC.presence_of_element_located(self._locator))

	def tap(self) -> None:
		"""
		Tap app element
		:return:
		"""

		'''
		element = WebDriverWait(self._driver, 5).until(
			EC.element_to_be_clickable(self._locator))
		'''

		if self._element.text not in '0123456789.':
			print("Tap '{}'".format(self._element.text))

		TouchAction(self._driver).tap(self._element).wait(3).perform()
		# element.click()
		return None

	@property
	def label(self):
		"""
		Returns text/label.
		:return:
		"""
		try:
			txt = self.string_formatter(self._element.text)
			txt = self.scientific_notation_to_integer_converter(txt)
			return txt
		except NoSuchAttributeException as err:
			print("ERROR: {}".format(err))
			return None

	@property
	def is_visible(self):
		"""
		Returns Boolean.
		Checks if element visible
		:return:
		"""
		return self._element.is_displayed()

	@staticmethod
	def string_formatter(data):
		"""
		Replace invalid characters with valid math operators:

		1. '−' >>> '-'
		2. '×' >>> '*'
		3. '÷' >>> '/'

		:param data:
		:return:
		"""

		if '−' in data:
			data = data.replace('−', '-')

		if '×' in data:
			data = data.replace('×', '*')

		if '÷' in data:
			data = data.replace('÷', '/')

		return data

	@staticmethod
	def scientific_notation_to_integer_converter(data) -> str:
		"""
		Convert scientific notation (string like '1e7') to an integer:
			In Python the e-form indicates a float, as does the presence of a
			decimal point, but you can convert to float and then to int: int(float('1e7')) >>> 10000000

		Source:
		https://mail.python.org/pipermail/python-list/2009-November/557390.html
		https://stackoverflow.com/questions/32861429/converting-number-in-scientific-notation-to-int

		Example:
			1e5 is a number expressed using scientific notation and it means
			10 to the 5th power (the e meaning 'exponent'), so 1e5 is equal to 100000,
			both notations are interchangeably meaning the same.

		Source: https://stackoverflow.com/questions/26174531/what-is-the-meaning-of-number-1e5
		:param data:
		:return:
		"""
		if 'E' not in data:
			return data
		else:
			print("Converting {} into int.".format(data))
			data = data.replace('.E', 'e')
			data.replace('E', 'e')
			data.replace('.', '')
			return str(int(float(data)))
