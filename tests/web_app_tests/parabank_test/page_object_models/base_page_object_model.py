"""Base Page Object Model Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from tests.web_app_tests.parabank_test.page_object_models.base_object_model import BaseObjectModel
from tests.web_app_tests.parabank_test.expected_results.page_content.base_page_content import BasePageContent


class BasePageObjectModel(BaseObjectModel):
	"""
	Base Page Object Model Class

	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	"""

	def __init__(self, config, driver, explicit_wait_time):

		super().__init__(driver=driver,
		                 explicit_wait_time=explicit_wait_time)
		self._config = config
		self._url = self._config.base_url + BasePageContent.URL

	@property
	def customer_login(self):
		"""
		Returns CustomerLoginModel instance
		:return:
		"""
		from tests.web_app_tests.parabank_test.page_object_models.customer_login_model import CustomerLoginModel
		customer_login = CustomerLoginModel(driver=self._driver,
		                                    config=self._config,
		                                    explicit_wait_time=self._explicit_wait_time)
		return customer_login

	def go(self):
		"""
		Opens test web page
		:return:
		"""

		print("\nGO: {}\n".format(self._url))
		self._driver.get(self._url)
		if self._driver.capabilities["automationName"] == 'Selenium':
			self._driver.maximize_window()
		return None

	def quit(self):
		"""
		Close web browser window (including all opened tabs)
		:return:
		"""
		if self._driver:
			self._driver.quit()
		return None

	def close(self):
		"""
		Close current tab
		:return:
		"""
		if self._driver:
			self._driver.close()
		return None

	@property
	def title(self):
		"""
		Returns web page title
		:return:
		"""
		return self._driver.title

	@property
	def url(self):
		"""
		Returns current URL
		:return:
		"""
		url = self._driver.current_url

		if ';' in url:
			url = url[:url.index(';')]

		if '?ConnType=JDBC' in url:
			url = url[:url.index('?ConnType=JDBC')]

		return url

	@staticmethod
	def _formatted_url(url: str):
		"""
		Removes following from href/url:
		1. https://parabank.parasoft.com/parabank/
		2. ;jsessionid=1219DE07E03D513449C6E1EEA9A73C43
		Result: images/clear.gif
		:param url:
		:return:
		"""

		url = url.replace(BasePageContent.URL, '')

		if ';' in url:
			if '?_wadl&_type=xml' in url:
				url = url[:url.index(';')] + '?_wadl&_type=xml'
			else:
				url = url[:url.index(';')]

		return url
