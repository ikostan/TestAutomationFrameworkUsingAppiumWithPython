"""Customer Login Locator Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from selenium.webdriver.common.by import By

from tests.web_app_tests.parabank_test.expected_results.page_content.register_page_content import RegisterPageContent


class CustomerLoginLocator:
	"""
	Customer Login Locator Class
	"""

	# Customer Login
	CUSTOMER_LOGIN_TITLE = (By.XPATH, '//*[@id="leftPanel"]/h2')
	# Username
	USERNAME_LOGIN_TITLE = (By.XPATH, '//*[@id="loginPanel"]/'
	                                  'form/p[1]/b')

	LOGIN_USERNAME_INPUT = (By.XPATH, '//*[@id="loginPanel"]/'
	                                  'form/'
	                                  'div[contains(@class, "login")]/'
	                                  'input[contains(@name, "username")]')
	# Password
	PASSWORD_LOGIN_TITLE = (By.XPATH, '//*[@id="loginPanel"]/'
	                                  'form/p[2]/b')

	LOGIN_PASSWORD_INPUT = (By.XPATH, '//*[@id="loginPanel"]/'
	                                  'form/'
	                                  'div[contains(@class, "login")]/'
	                                  'input[contains(@name, "password")]')
	# Button
	CUSTOMER_LOGIN_BUTTON = (By.XPATH, '//*[@id="loginPanel"]/'
	                                   'form/'
	                                   'div[contains(@class, "login")]/'
	                                   'input[contains(@type, "submit")]')

	FORGOT_LOGIN = (By.XPATH, '//*[@id="loginPanel"]/p/'
	                          'a[contains(@href, "lookup.htm")]')

	REGISTER = (By.XPATH, '//*[@id="loginPanel"]/p/'
	                      'a[contains(@href, "{}")]'.format(RegisterPageContent.BASE_URL))
