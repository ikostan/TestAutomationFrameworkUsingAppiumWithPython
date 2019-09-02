""" Footer Menu Locator Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from selenium.webdriver.common.by import By

from tests.web_app_tests.parabank_test.expected_results.page_content.home_page_content import HomePageContent
from tests.web_app_tests.parabank_test.expected_results.page_content.about_page_content import AboutPageContent
from tests.web_app_tests.parabank_test.expected_results.page_content.contact_page_content import ContactPageContent
from tests.web_app_tests.parabank_test.expected_results.page_content.site_map_page_content import SiteMapPageContent
from tests.web_app_tests.parabank_test.expected_results.page_content.services_page_content import ServicesPageContent


class FooterMenuLocator:
	"""
	Footer Menu Locator Class
	"""

	# Footer
	FOOTER_HOME = (By.XPATH, '//*[@id="footerPanel"]/ul[1]/li[1]/'
	                         'a[contains(@href, "{}")]'.format(HomePageContent.URL))

	FOOTER_ABOUT_US = (By.XPATH, '//*[@id="footerPanel"]/'
	                             'ul[1]/li[2]/'
	                             'a[contains(@href, "{}")]'.format(AboutPageContent.BASE_URL))

	FOOTER_SERVICES = (By.XPATH, '//*[@id="footerPanel"]/'
	                             'ul[1]/li[3]/'
	                             'a[contains(@href, "{}")]'.format(ServicesPageContent.BASE_URL))

	FOOTER_PRODUCTS = (By.XPATH, '//*[@id="footerPanel"]/'
	                             'ul[1]/li[4]/'
	                             'a[contains(@href, "http://www.parasoft.com/jsp/products.jsp")]')

	FOOTER_LOCATIONS = (By.XPATH, '//*[@id="footerPanel"]/'
	                              'ul[1]/li[5]/a')

	FOOTER_FORUM = (By.XPATH, '//*[@id="footerPanel"]/'
	                          'ul[1]/li[6]/'
	                          'a[contains(@href, "http://forums.parasoft.com/")]')

	FOOTER_SITE_MAP = (By.XPATH, '//*[@id="footerPanel"]/'
	                             'ul[1]/li[7]/'
	                             'a[contains(@href, "{}")]'.format(SiteMapPageContent.URL))

	FOOTER_CONTACT_US = (By.XPATH, '//*[@id="footerPanel"]/'
	                               'ul[1]/li[8]/'
	                               'a[contains(@href, "{}")]'.format(ContactPageContent.URL))

	FOOTER_COPYRIGHT = (By.XPATH, '//*[@id="footerPanel"]/'
	                              'p[contains(@class, "copyright")]')

	FOOTER_VISIT_US = (By.XPATH, '//*[@id="footerPanel"]/ul[contains(@class, "visit")]/li[1]')

	FOOTER_VISIT_US_LINK = (By.XPATH, '//*[@id="footerPanel"]/'
	                                  'ul[contains(@class, "visit")]/li/'
	                                  'a[contains(@href, "http://www.parasoft.com/")]')

