"""Register User helper method"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


import time
import allure

from tests.web_app_tests.parabank_test.page_object_models.register_page_model import RegisterPageModel


def register_user(driver, user, config):
    """
    Register User helper method

    Registers a new user.
    Does not check for any errors.
    Using Selenium WebDriver + Chrome browser by default
    :param driver:
    :param config:
    :param page:
    :param user:
    :return:
    """

    print("\nUser registration procedure...")
    print("\n1. Open web browser...")
    page = RegisterPageModel(config=config,
                             driver=driver,
                             explicit_wait_time=10)
    # Open Web page
    with allure.step("Open Register web page"):
        page.go()

    with allure.step("Fill out Register web form"):
        print("\n2. Filling out user data...")

        page.personal_info.type_first_name(user.first_name)

        page.personal_info.type_last_name(user.last_name)

        page.personal_info.type_address(user.address)

        page.personal_info.type_city(user.city)

        page.personal_info.type_state(user.state)

        page.personal_info.type_zip_code(user.zip_code)

        page.personal_info.type_phone(user.phone)

        page.personal_info.type_ssn(user.ssn)

        page.type_username(user.username)

        page.type_password(user.password)

        page.type_confirm(user.password)

    with allure.step("Hit 'REGISTER' button"):
        print("\n3. Hit 'REGISTER' button...")
        page = page.hit_register_btn()
        time.sleep(3)

    with allure.step("Do Log Out"):
        print("\n4. Do Log Out...")
        page.hit_log_out_button()
        time.sleep(3)

    with allure.step("Close web browser"):
        print("\n5. Close web browser...")
        # page.quit()
        pass

