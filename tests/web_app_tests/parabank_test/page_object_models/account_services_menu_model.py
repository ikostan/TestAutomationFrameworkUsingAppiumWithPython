"""Account Services Menu Model Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.web_app_tests.parabank_test.page_object_models.home_page_model import HomePageModel
from tests.web_app_tests.parabank_test.page_object_models.base_object_model import BaseObjectModel
from tests.web_app_tests.parabank_test.page_locators.account_services_menu_locator import AccountServicesMenuLocator


class AccountServicesMenuModel(BaseObjectModel):
	"""
	Account Services Menu Model Class
	"""

	def __init__(self, config, driver, explicit_wait_time):

		super().__init__(driver=driver, explicit_wait_time=explicit_wait_time)
		self._config = config
		self._locator = AccountServicesMenuLocator

	@property
	def locator(self):
		return self._locator

	@property
	def welcome_message(self):
		"""
		Returns Welcome message text
		:return:
		"""
		element = self.create_web_element(self.locator.WELCOME_MESSAGE)
		return element.text

	@property
	def menu_title(self):
		"""
		Returns Account Services menu title
		:return:
		"""
		element = self.create_web_element(self.locator.ACCOUNT_SERVICES_HEADER)
		return element.text

	def hit_log_out_button(self):
		"""
		1. Click on "Log Out"
		2. Wait until URL changes
		3. Returns HomePageModel on success
		4. Return TimeoutException on failure
		An expectation for checking the current url.
        url is the expected url, which must not be an exact match
        returns True if the url is different, false otherwise.

        Source: https://seleniumhq.github.io/selenium/docs/api/py
        /_modules/selenium/webdriver/support/expected_conditions.html#url_changes
		:return:
		"""

		current_url = self._driver.current_url

		locator = self._locator.LOG_OUT
		element = self.create_web_element(locator)

		element.click_on()

		WebDriverWait(self.driver,
		              self.explicit_wait_time).until(EC.url_changes(current_url))

		return HomePageModel(config=self._config,
		                     driver=self.driver,
		                     explicit_wait_time=self.explicit_wait_time)
