"""Forgot Login Info Page Locator Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from selenium.webdriver.common.by import By

from tests.web_app_tests.parabank_test.page_locators.base_page_locator import BasePageLocator


class ForgotLoginInfoPageLocator(BasePageLocator, BasePersonalInfoPageLocator):
	"""
	Holds all relevant locators for 'Forgot Login Info' page web elements.
	Each locator is a tuple.
	Separate the locator strings from the place where they are being used.
	"""

	FIND_MY_LOGIN_INFO_BUTTON = (By.XPATH,
	                             '//input[contains(@value, "Find My Login Info")]')

	USERNAME_PASSWORD = (By.XPATH, '//*[@id="rightPanel"]/p[2]')

	ERROR_TITLE = (By.XPATH, '//*[@id="rightPanel"]/h1')

	ERROR_MESSAGE = (By.XPATH, '//*[@id="rightPanel"]/p')

