"""Home Page Model Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from utils.driver import Driver
from tests.config import Config

from tests.web_app_tests.parabank_test.page_locators.home_page_locator import HomePageLocator
from tests.web_app_tests.parabank_test.page_object_models.base_page_object_model import BasePageObjectModel
from tests.web_app_tests.parabank_test.expected_results.page_content.home_page_content import HomePageContent


class HomePageModel(BasePageObjectModel):
	"""
	Home Page Model Class

	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	"""

	def __init__(self, config: Config, driver: Driver, explicit_wait_time):

		super().__init__(config=config,
		                 driver=driver,
		                 explicit_wait_time=explicit_wait_time)
		self._url = config.base_url + HomePageContent.URL
		self._locator = HomePageLocator

	@property
	def atm_title(self):
		"""
		Returns title from ATM Services section
		:return:
		"""
		locator = self._locator.ATM_SERVICES_TITLE
		return self.get_text_property(locator)

	@property
	def atm_withdraw_funds_text(self):
		"""
		Returns withdraw funds text from ATM Services section
		:return:
		"""
		locator = self._locator.WITHDRAW_FUNDS
		return self.get_text_property(locator)

	@property
	def atm_transfer_funds_text(self):
		"""
		Returns transfer funds text from ATM Services section
		:return:
		"""
		locator = self._locator.ATM_TRANSFER_FUNDS
		return self.get_text_property(locator)

	@property
	def atm_check_balances_text(self):
		"""
		Returns check_balances_text from ATM Services section
		:return:
		"""
		locator = self._locator.CHECK_BALANCES
		return self.get_text_property(locator)

	@property
	def atm_make_deposits_text(self):
		"""
		Returns make_deposits_text from ATM Services section
		:return:
		"""
		locator = self._locator.MAKE_DEPOSITS
		return self.get_text_property(locator)

	@property
	def online_services_title(self):
		"""
		Returns title from online_services section
		:return:
		"""
		locator = self._locator.ONLINE_SERVICES_TITLE
		return self.get_text_property(locator)

	@property
	def bill_pay_title(self):
		"""
		Returns title from bill_pay section
		:return:
		"""
		locator = self._locator.BILL_PAY
		return self.get_text_property(locator)

	@property
	def account_history_title(self):
		"""
		Returns title from account_history section
		:return:
		"""
		locator = self._locator.ACCOUNT_HISTORY
		return self.get_text_property(locator)

	@property
	def online_transfer_funds_title(self):
		"""
		Returns title from transfer_funds section
		:return:
		"""
		locator = self._locator.ONLINE_TRANSFER_FUNDS
		return self.get_text_property(locator)

	@property
	def read_more_services_title(self):
		"""
		Returns title from read_more_services section
		:return:
		"""
		locator = self._locator.READ_MORE_SERVICES
		return self.get_text_property(locator)

	@property
	def read_more_news_title(self):
		"""
		Returns title from read_more_news section
		:return:
		"""
		locator = self._locator.READ_MORE_NEWS
		return self.get_text_property(locator)

	@property
	def latest_news_title(self):
		"""
		Returns title from latest_news section
		:return:
		"""
		locator = self._locator.LATEST_NEWS
		return self.get_text_property(locator)
