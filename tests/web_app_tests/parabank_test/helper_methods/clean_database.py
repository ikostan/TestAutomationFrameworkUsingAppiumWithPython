"""Clean DB helper method"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import time
import allure

from tests.config import Config
from tests.web_app_tests.parabank_test.page_object_models.admin_page_model import AdminPageModel


def clean_database(driver, config: Config):
	"""
	Clean and initialise database.
	Does not check for any errors.
	:return:
	"""

	print("Open web browser")
	page = AdminPageModel(config=config,
	                      driver=driver,
	                      explicit_wait_time=10)
	# Open Web page
	with allure.step("Open Admin web page"):
		page.go()

	with allure.step("Press 'CLEAN' button"):
		print("\nCleaning database...")
		page.clean_button.click_on()
		time.sleep(2)

	with allure.step("Press 'INITIALIZE' button"):
		print("\nInitializing database...")
		page.initialize_button.click_on()
		time.sleep(2)

	with allure.step("Close web browser"):
		print("\n5. Close web browser...")
		# page.quit()
		pass
