"""Accounts Overview Page Model Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from tests.config import Config
from utils.driver import Driver

from tests.web_app_tests.parabank_test.page_object_models.base_page_object_model import BasePageObjectModel
from tests.web_app_tests.parabank_test.page_locators.accounts_overview_page_locator import AccountsOverviewPageLocator
from tests.web_app_tests.parabank_test.expected_results.page_content.accounts_overview_page_content import \
	AccountsOverviewPageContent


class AccountsOverviewPageModel(BasePageObjectModel):
	"""
	Accounts Overview Page Model Class
	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	"""

	def __init__(self, config: Config, driver: Driver, explicit_wait_time):

		super().__init__(config=config,
		                 driver=driver,
		                 explicit_wait_time=explicit_wait_time)

		self._locator = AccountsOverviewPageLocator
		_url = config.base_url + AccountsOverviewPageContent.URL

	@property
	def total_balance(self):
		"""
		Returns total balance value
		:return:
		"""
		locator = self._locator.TOTAL_VALUE
		return self.get_text_property(locator)


