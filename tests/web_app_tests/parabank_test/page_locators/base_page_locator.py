"""Base Page Locator Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from selenium.webdriver.common.by import By

from tests.web_app_tests.parabank_test.expected_results.page_content.admin_page_content import AdminPageContent
from tests.web_app_tests.parabank_test.expected_results.page_content.home_page_content import HomePageContent


class BasePageLocator:
	"""
	Base Page Locator Class

	Holds all relevant locators for any page web elements.
	Each locator is a tuple.
	Separate the locator strings from the place where they are being used.
	"""

	# Admin Logo:
	ADMIN_LOGO_HREF = (By.XPATH, '//*[@id="topPanel"]/'
	                             'a[contains(@href,"{}")]'.format(AdminPageContent.URL))

	ADMIN_LOGO_IMG = (By.XPATH, '//*[@id="topPanel"]/'
	                            'a[contains(@href,"{}")]/img'.format(AdminPageContent.URL))

	# ParaBank Logo:
	PARA_BANK_LOGO_HREF = (By.XPATH, '//*[@id="topPanel"]/'
	                                 'a[contains(@href,"/'
	                                 '{}")]'.format(HomePageContent.URL))

	PARA_BANK_LOGO_IMG = (By.XPATH, '//*[@id="topPanel"]/'
	                                'a[contains(@href,"/'
	                                '{}")]/'
	                                'img[contains(@class,"logo")]'.format(HomePageContent.URL))

	SLOGAN = (By.XPATH, '//*[@id="topPanel"]/'
	                    'p[contains(@class,"caption")]')

	# Menu Buttons:
	HOME_BUTTON = (By.XPATH, '//*[@id="headerPanel"]/'
	                         'ul[contains(@class,"button")]/'
	                         'li[contains(@class,"home")]/a')

	ABOUT_BUTTON = (By.XPATH, '//*[@id="headerPanel"]/'
	                          'ul[contains(@class,"button")]/'
	                          'li[contains(@class,"aboutus")]/a')

	CONTACT_BUTTON = (By.XPATH, '//*[@id="headerPanel"]/'
	                            'ul[contains(@class,"button")]/'
	                            'li[contains(@class,"contact")]/a')

	# Account Services
	BILL_PAY = (By.XPATH,
	            '//a[contains(text(), "Bill Pay")]')

	ACCOUNTS_OVERVIEW = (By.XPATH,
	                     '//a[contains(text(), "Accounts Overview")]')


