"""Accounts Overview Page Locator Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from selenium.webdriver.common.by import By

from tests.web_app_tests.parabank_test.expected_results.page_content.account_overview_content import \
	AccountOverviewContent
from tests.web_app_tests.parabank_test.page_locators.base_page_locator import BasePageLocator


class AccountsOverviewPageLocator(BasePageLocator):
	"""
	Accounts Overview Page Locator Class

	Holds all relevant locators for 'Accounts Overview' page web elements.
	Each locator is a tuple.
	Separate the locator strings from the place where they are being used.
	"""

	HEADER = (By.XPATH, '//h1[@innertext=\'{}\']'.format(AccountOverviewContent.HEADER))

	TOTAL_VALUE = (By.XPATH, '//b[contains(text(), \'$\')]')
