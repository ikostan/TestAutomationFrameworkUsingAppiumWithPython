"""Base Element Definition"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchAttributeException


class BaseElement:

	def __init__(self, driver, locator: tuple):
		self._driver = driver
		self._locator = locator
		self._element = self._set_element()

	def _set_element(self):
		return WebDriverWait(self._driver, 5).until(
			EC.presence_of_element_located(self._locator))

	def tap(self) -> None:
		"""
		Tap on app element
		:return:
		"""
		element = WebDriverWait(self._driver, 5).until(
			EC.element_to_be_clickable(self._locator))
		element.click()
		return None

	@property
	def label(self):
		"""
		Returns text/label.
		:return:
		"""
		try:
			txt = self.string_formatter(self._element.text)
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

		:param data:
		:return:
		"""

		if '−' in data:
			data = data.replace('−', '-')

		return data
