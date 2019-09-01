"""Register Page Model Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from utils.driver import Driver
from tests.config import Config

from tests.web_app_tests.parabank_test.page_object_models.base_page_model import BasePageModel
from tests.web_app_tests.parabank_test.page_locators.register_page_locator import RegisterPageLocator
from tests.web_app_tests.parabank_test.expected_results.page_content.register_page_content import RegisterPageContent
from tests.web_app_tests.parabank_test.page_object_models.base_personal_info_page_model import BasePersonalInfoPageModel


class RegisterPageModel(BasePageModel):
	"""
	Register Page Model Class

	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	"""

	def __init__(self, config: Config, driver: Driver, implicit_wait_time, explicit_wait_time):
		super().__init__(config, driver, implicit_wait_time, explicit_wait_time)

		self._url = config.base_url + RegisterPageContent.URL
		self.personal_info = BasePersonalInfoPageModel(driver=driver,
		                                               explicit_wait_time=explicit_wait_time)
		self._locator = RegisterPageLocator

	@property
	def username_title(self):
		"""
		Returns username title text
		:return:
		"""
		locator = self._locator.USERNAME_TITLE
		element = self.create_web_element(locator)
		txt = element.text
		return txt

	def type_username(self, username: str):
		"""
		Write text into username input field
		:param username:
		:return:
		"""
		locator = self._locator.USERNAME_INPUT
		element = self.create_web_element(locator)
		element.write(username)
		return None

	@property
	def username(self):
		"""
		Return value from username input field
		:return:
		"""
		locator = self._locator.USERNAME_INPUT
		element = self.create_web_element(locator)
		value = element.element_value
		return value

	@property
	def username_error(self):
		"""
		Returns Username error.
		:return:
		"""
		locator = self._locator.USERNAME_ERROR
		element = self.create_web_element(locator)
		txt = element.text
		return txt

	@property
	def password_title(self):
		"""
		Returns password title text
		:return:
		"""
		locator = self._locator.PASSWORD_TITLE
		element = self.create_web_element(locator)
		txt = element.text
		return txt

	def type_password(self, password: str):
		"""
		Write text into password input field
		:param password:
		:return:
		"""
		locator = self._locator.PASSWORD_INPUT
		element = self.create_web_element(locator)
		element.write(password)
		return None

	@property
	def password(self):
		"""
		Return value from password input field
		:return:
		"""
		locator = self._locator.PASSWORD_INPUT
		element = self.create_web_element(locator)
		value = element.element_value
		return value

	@property
	def password_error(self):
		"""
		Returns Username error.
		:return:
		"""
		locator = self._locator.PASSWORD_ERROR
		element = self.create_web_element(locator)
		txt = element.text
		return txt

	@property
	def confirm_title(self):
		"""
		Returns confirm title text
		:return:
		"""
		locator = self._locator.CONFIRM_TITLE
		element = self.create_web_element(locator)
		txt = element.text
		return txt

	def type_confirm(self, password: str):
		"""
		Write text into confirm input field
		:param password:
		:return:
		"""
		locator = self._locator.CONFIRM_INPUT
		element = self.create_web_element(locator)
		element.write(password)
		return None

	@property
	def confirm(self):
		"""
		Return value from confirm input field
		:return:
		"""
		locator = self._locator.CONFIRM_INPUT
		element = self.create_web_element(locator)
		value = element.element_value
		return value

	@property
	def confirm_error(self):
		"""
		Returns Confirm error.
		Non in case error does not appear.
		:return:
		"""
		locator = self._locator.CONFIRM_ERROR
		element = self.create_web_element(locator)
		txt = element.text
		return txt

	@property
	def register_btn_label(self):
		"""
		Returns register button label
		:return:
		"""
		locator = self._locator.REGISTER_BUTTON
		element = self.create_web_element(locator)
		txt = element.element_value
		return txt

	@property
	def register_btn_class(self):
		"""
		Returns register button class
		:return:
		"""
		locator = self._locator.REGISTER_BUTTON
		element = self.create_web_element(locator)
		txt = element.element_class
		return txt

	@property
	def register_btn_type(self):
		"""
		Returns register button type
		:return:
		"""
		locator = self._locator.REGISTER_BUTTON
		element = self.create_web_element(locator)
		txt = element.element_type
		return txt

	def hit_register_btn(self):
		"""
		Click on register button
		:return:
		"""
		locator = self._locator.REGISTER_BUTTON
		element = self.create_web_element(locator)
		element.click_on()
		return RegisterPageModel(config=self._config,
		                         driver=self.driver,
		                         implicit_wait_time=5,
		                         explicit_wait_time=10)

	@property
	def welcome_header(self):
		"""
		Returns welcome header
		:return:
		"""
		locator = self._locator.HEADER
		element = self.create_web_element(locator)
		value = element.text
		return value

	@property
	def welcome_message(self):
		"""
		Returns welcome message
		:return:
		"""
		locator = self._locator.DESCRIPTION
		element = self.create_web_element(locator)
		value = element.text
		return value
