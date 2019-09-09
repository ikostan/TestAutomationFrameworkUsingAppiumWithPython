"""Admin Page Model Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from utils.driver import Driver

from tests.config import Config
from tests.web_app_tests.parabank_test.page_locators.admin_page_locator import AdminPageLocator
from tests.web_app_tests.parabank_test.page_object_models.base_page_object_model import BasePageObjectModel
from tests.web_app_tests.parabank_test.expected_results.page_content.admin_page_content import AdminPageContent


class AdminPageModel(BasePageObjectModel):
	"""
	Admin Page Model Class

	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	"""

	def __init__(self, config: Config, driver: Driver, explicit_wait_time):

		super().__init__(config, driver, explicit_wait_time)

		self._url = config.base_url + AdminPageContent.URL
		self._locator = AdminPageLocator

	@property
	def initialize_button(self):
		"""
		Returns Initialize button
		:return:
		"""

		locator = self._locator.INITIALIZE_BUTTON
		element = self.create_web_element(locator)
		return element

	@property
	def clean_button(self):
		"""
		Returns Clean button
		:return:
		"""

		locator = self._locator.CLEAN_BUTTON
		element = self.create_web_element(locator)
		return element
