"""Customer Login Model Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.web_app_tests.parabank_test.page_object_models.base_object_model import BaseObjectModel
from tests.web_app_tests.parabank_test.page_locators.customer_login_locator import CustomerLoginLocator
from tests.web_app_tests.parabank_test.expected_results.page_content.login_page_content import LoginPageContent
from tests.web_app_tests.parabank_test.expected_results.page_content.accounts_overview_page_content import \
	AccountsOverviewPageContent


class CustomerLoginModel(BaseObjectModel):
	"""
	Customer Login Model Class
	Holds elements from Customer Login section
	"""

	def __init__(self, driver, config, explicit_wait_time):

		super().__init__(driver=driver,
		                 explicit_wait_time=explicit_wait_time)
		self._locator = CustomerLoginLocator
		self._config = config

	@property
	def customer_login_title(self):
		"""
		Returns customer login title
		:return:
		"""
		locator = self._locator.CUSTOMER_LOGIN_TITLE
		return self.get_text_property(locator)

	@property
	def username_login_title(self):
		"""
		Returns username login title
		:return:
		"""
		locator = self._locator.USERNAME_LOGIN_TITLE
		return self.get_text_property(locator)

	@property
	def password_login_title(self):
		"""
		Returns password login title
		:return:
		"""
		locator = self._locator.PASSWORD_LOGIN_TITLE
		return self.get_text_property(locator)

	@property
	def username(self):
		"""
		Returns Username field value
		:return:
		"""
		locator = self._locator.LOGIN_USERNAME_INPUT
		element = self.create_web_element(locator)
		value = element.element_value
		return value

	def enter_username(self, username):
		"""
		Type username into Username input field
		:return:
		"""
		locator = self._locator.LOGIN_USERNAME_INPUT
		element = self.create_web_element(locator)
		element.write(username)
		return None

	@property
	def password(self):
		"""
		Returns Password field value
		:return:
		"""
		locator = self._locator.LOGIN_PASSWORD_INPUT
		element = self.create_web_element(locator)
		value = element.element_value
		return value

	def enter_password(self, password):
		"""
		Type password into Password input field
		:return:
		"""
		locator = self._locator.LOGIN_PASSWORD_INPUT
		element = self.create_web_element(locator)
		element.write(password)
		return None

	@property
	def login_button_value(self):
		"""
		Returns login_button value
		:return:
		"""
		locator = self._locator.CUSTOMER_LOGIN_BUTTON
		element = self.create_web_element(locator)
		atr = element.element_value
		return atr

	def hit_login_button(self):
		"""
		1. Click on Log In button
		2. Wait until URL changes
		3. Returns OverviewPageModel object on success
		4. Return TimeOut exception on failure
		:return:
		"""
		locator = self._locator.CUSTOMER_LOGIN_BUTTON
		element = self.create_web_element(locator)
		current_url = self._driver.current_url
		element.click_on()
		WebDriverWait(self._driver, self._explicit_wait_time).until(EC.url_changes(current_url))

		if self._driver.current_url == self._config.base_url + AccountsOverviewPageContent.URL:
			from tests.web_app_tests.parabank_test.page_object_models.accounts_overview_page_model import \
				AccountsOverviewPageModel
			return AccountsOverviewPageModel(config=self._config,
			                                 driver=self._driver,
			                                 explicit_wait_time=10)

		if self._driver.current_url == self._config.base_url + LoginPageContent.URL:
			from tests.web_app_tests.parabank_test.page_object_models.login_page_model import LoginPageModel
			return LoginPageModel(config=self._config,
			                      driver=self._driver,
			                      explicit_wait_time=10)

		raise Exception("Unknown URL: {} > Flow is not implemented".format(self._driver.current_url))

	@property
	def forgot_login(self):
		"""
		Returns forgot login web element
		:return:
		"""
		locator = self._locator.FORGOT_LOGIN
		element = self.create_web_element(locator)
		return element

	@property
	def register(self):
		"""
		Returns register web element
		:return:
		"""
		locator = self._locator.REGISTER
		element = self.create_web_element(locator)
		return element

