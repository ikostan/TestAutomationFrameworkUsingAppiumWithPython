"""Open Web Browser helper method"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure

from tests.config import Config
from utils.driver import Driver
from utils.get_args_from_cli import get_args


def open_web_browser(config: Config, page_model, page_content):
	"""
	Take care of following procedure:
		1. Instantiate Selenium webdriver
		2. Instantiate Page Model Object
		3. Checks HTTP status code
		4. Open web browser > open test web page
		5. Refresh web browser in case test web site is not loaded
		6. Returns page instance (Page Model Object)
	:param config:
	:param page_model:
	:param page_content:
	:return:
	"""

	# Open web page
	with allure.step("Open following web page: {}.".format(page_content.URL)):
		driver = Driver()
		print('\nbase_url: {}\n'.format(config.base_url))

		args = get_args()
		for key in args:
			driver.set_capability(key, args[key])

		page = page_model(config=config, driver=driver, implicit_wait_time=5, explicit_wait_time=10)
		page.go()
		return page

