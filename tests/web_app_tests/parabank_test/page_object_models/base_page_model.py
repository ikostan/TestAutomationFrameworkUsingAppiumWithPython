"""Base Page Object Model"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePageModel:
	'''
	Base Page Object Model

	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	'''

	def __init__(self, driver, implicit_wait_time, explicit_wait_time):
		self._implicit_wait_time = implicit_wait_time
		self._explicit_wait_time = explicit_wait_time
		self._driver = driver
		self._set_implicit_wait(implicit_wait_time)

	def _set_implicit_wait(self, implicit_wait_time: int):
		'''
		The default value of time that can be set using Implicit wait is zero.
		Its unit is in seconds.
		Implicit wait remains associated with the web element until it gets destroyed.
		:param implicit_wait_time:
		:return:
		'''
		if type(implicit_wait_time) != int:
			raise TypeError('\nERROR: wrong data type. Please set "implicit_wait_time" value as integer.\n')
		self._driver.implicitly_wait(implicit_wait_time)
		return None

	@property
	def implicit_wait_time(self):
		return self._implicit_wait_time

	@property
	def explicit_wait_time(self):
		return self._explicit_wait_time

	def go(self):
		'''
		Opens test web page
		:return:
		'''

		self._driver.get(self._url)
		self._driver.maximize_window()
		return None

	def quit(self):
		'''
		Close web browser window (including all opened tabs)
		:return:
		'''
		if self._driver:
			self._driver.quit()
		return None

	def close(self):
		'''
		Close current tab
		:return:
		'''
		if self._driver:
			self._driver.close()
		return None

	@property
	def driver(self):
		'''
		Returns Selenium webdriver object
		:return:
		'''
		return self._driver

	@property
	def title(self):
		'''
		Returns web page title
		:return:
		'''
		return self._driver.title

	@property
	def url(self):
		'''
		Returns current URL
		:return:
		'''
		url = self._driver.current_url

		if ';' in url:
			url = url[:url.index(';')]

		if '?ConnType=JDBC' in url:
			url = url[:url.index('?ConnType=JDBC')]

		return url

	@staticmethod
	def _formated_url(url: str):
		'''
		Removes following from href/url:
		1. https://parabank.parasoft.com/parabank/
		2. ;jsessionid=1219DE07E03D513449C6E1EEA9A73C43
		Result: images/clear.gif
		:param url:
		:return:
		'''
		url = url.replace(BasePageContent.URL, '')

		if ';' in url:
			if '?_wadl&_type=xml' in url:
				url = url[:url.index(';')] + '?_wadl&_type=xml'
			else:
				url = url[:url.index(';')]

		return url

