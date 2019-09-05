"""Base Object Model Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from tests.web_app_tests.parabank_test.element_object_model.element import Element


class BaseObjectModel:
	"""
	Base Object Model Class
	"""

	def __init__(self, driver, explicit_wait_time):
		self._explicit_wait_time = explicit_wait_time
		self._driver = driver

	@property
	def explicit_wait_time(self):
		return self._explicit_wait_time

	@property
	def driver(self):
		"""
		Returns Selenium webdriver object
		:return:
		"""
		return self._driver

	def create_web_element(self, locator):
		"""
		Returns base web element
		:param locator:
		:return:
		"""
		return Element(driver=self._driver,
		               explicit_wait_time=self._explicit_wait_time,
		               locator=locator)

	def get_text_property(self, locator):
		"""
		Returns web element's text property
		:param locator:
		:return:
		"""
		element = self.create_web_element(locator)
		txt = element.text
		return txt

	def get_value_property(self, locator):
		"""
		Returns web element's text property
		:param locator:
		:return:
		"""
		element = self.create_web_element(locator)
		txt = element.element_value
		return txt
