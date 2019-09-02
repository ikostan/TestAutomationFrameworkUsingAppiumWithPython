"""Solutions Menu Locator Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from selenium.webdriver.common.by import By

from tests.web_app_tests.parabank_test.expected_results.page_content.about_page_content import AboutPageContent
from tests.web_app_tests.parabank_test.expected_results.page_content.admin_page_content import AdminPageContent
from tests.web_app_tests.parabank_test.expected_results.page_content.services_page_content import ServicesPageContent


class SolutionsMenuLocator:
	"""
	Solutions Menu Locator Class
	"""

	# Solutions Menu:
	SOLUTIONS = (By.XPATH, '//*[@id="headerPanel"]/'
	                       'ul[contains(@class,"leftmenu")]/'
	                       'li[contains(@class,"Solutions")]')

	ABOUT_US_MENU_ITEM = (By.XPATH, '//*[@id="headerPanel"]/'
	                                'ul[contains(@class,"leftmenu")]/'
	                                'li[2]/'
	                                'a[contains(@href, "{}")]'.format(AboutPageContent.BASE_URL))

	SERVICES_MENU_ITEM = (By.XPATH, '//*[@id="headerPanel"]/'
	                                'ul[contains(@class,"leftmenu")]/'
	                                'li[3]/'
	                                'a[contains(@href, "{}")]'.format(ServicesPageContent.BASE_URL))

	PRODUCTS_MENU_ITEM = (By.XPATH, '//*[@id="headerPanel"]/'
	                                'ul[contains(@class,"leftmenu")]/'
	                                'li[4]/'
	                                'a[contains(@href, "http://www.parasoft.com/jsp/products.jsp")]')

	LOCATIONS_MENU_ITEM = (By.XPATH, '//*[@id="headerPanel"]/'
	                                 'ul[contains(@class,"leftmenu")]/'
	                                 'li[5]/'
	                                 'a[contains(@href, "http://www.parasoft.com/jsp/pr/contacts.jsp")]')

	ADMIN_PAGE_MENU_ITEM = (By.XPATH, '//*[@id="headerPanel"]/'
	                                  'ul[contains(@class,"leftmenu")]/'
	                                  'li[6]/'
	                                  'a[contains(@href, "{}")]'.format(AdminPageContent.BASE_URL))
