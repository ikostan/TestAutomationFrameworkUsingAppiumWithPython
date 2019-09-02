"""Account Services Menu Model Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.web_app_tests.parabank_test.element_object_model.element import Element
from tests.web_app_tests.parabank_test.page_object_models.home_page_model import HomePageModel
from tests.web_app_tests.parabank_test.page_locators.account_services_menu_locator import AccountServicesMenuLocator


class AccountServicesMenuModel:
	"""
	Account Services Menu Model Class
	"""

	def __init__(self, config, driver, implicit_wait_time=5, explicit_wait_time=10):

		self._config = config
		self._driver = driver
		self._implicit_wait_time = implicit_wait_time
		self._explicit_wait_time = explicit_wait_time

	def hit_log_out_button(self):
		"""
		1. Click on "Log Out"
		2. Wait until URL changes
		3. Returns HomePageModel on success
		4. Return TimeoutException on failure
		An expectation for checking the current url.
        url is the expected url, which must not be an exact match
        returns True if the url is different, false otherwise.
        Source: https://seleniumhq.github.io/selenium/docs/api/py/_modules/selenium/webdriver/support/expected_conditions.html#url_changes
		:return:
		"""

		current_url = self._driver.current_url

		element = Element(self._driver,
		                  self._explicit_wait_time,
		                  AccountServicesMenuLocator.LOG_OUT)

		element.click_on()

		WebDriverWait(self._driver, self._explicit_wait_time).until(EC.url_changes(current_url))

		return HomePageModel(config=self._config,
		                     driver=self._driver,
		                     implicit_wait_time=5,
		                     explicit_wait_time=10)
