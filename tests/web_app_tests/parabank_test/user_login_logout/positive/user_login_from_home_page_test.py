"""Test User Login From Admin Page Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import pytest

from utils.get_args_from_cli import get_args
from selenium.common.exceptions import NoSuchElementException

from tests.config import Config
from tests.web_app_tests.parabank_test.expected_results.users.base_user import BaseUser
from tests.web_app_tests.parabank_test.helper_methods.register_user import register_user
from tests.web_app_tests.android_browser_base_testcase import AndroidBrowserBaseTestCase
from tests.web_app_tests.parabank_test.helper_methods.clean_database import clean_database
from tests.web_app_tests.parabank_test.page_object_models.home_page_model import HomePageModel
from tests.web_app_tests.parabank_test.expected_results.users.valid_users_templates.jane_doe import JaneDoe
from tests.web_app_tests.parabank_test.expected_results.page_content.home_page_content import HomePageContent
from tests.web_app_tests.parabank_test.page_object_models.account_services_menu_model import AccountServicesMenuModel
from tests.web_app_tests.parabank_test.expected_results.page_content.accounts_overview_page_content import \
    AccountsOverviewPageContent


@allure.epic('Page Functionality')
@allure.parent_suite('End To End')
@allure.suite("User Login/Logout")
@allure.sub_suite("Positive Tests")
@allure.feature("Home Page")
@allure.story('Login/Logout Functionality')
@pytest.mark.skipif(get_args()['env'] == 'production',
                    reason="This is demo test that usually fails on production environment. "
                           "Therefore, it will have negative effect on Travis CI status.")
class TestUserLoginFromHomePage(AndroidBrowserBaseTestCase):
    """
    Test User Login From Admin Page Class
    """

    def test_user_login_logout(self):
        allure.dynamic.description("""
                User Log In validation > Login from Home page:
                    
                    Prerequisites: DB is clean, user is registered, web browser is opened
                    
                    Step by step:
                    1. Open Home web page
                    2. Do URL verification
                    3. Do Title verification
                    4. Type username/password
                    5. Hit "Log In" button
                    6. Verify "Welcome" message
                    7. Verify that "Account Services" menu title is present
                    8. Do URL verification
                    9. Log Out
                    10. Do URL verification
                    11. Verify that "Account Services" menu is not present
                    12. Verify web page title
                    13. Close web browser
                """)
        allure.dynamic.title("Admin Page > User Log In validation > Positive test")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        config = Config()
        user = BaseUser(JaneDoe)

        with allure.step("Initial data setup > clean DB"):
            clean_database(driver=self.driver,
                           config=config)

        with allure.step("Initial data setup > register test user"):
            register_user(driver=self.driver,
                          user=user,
                          config=config)

        with allure.step("Open web browser"):
            page = HomePageModel(config=config,
                                 driver=self.driver,
                                 explicit_wait_time=10)

        # 1. Open Home web page
        with allure.step("Open web page"):
            page.go()

        # 2. Do URL verification
        with allure.step("Verify web page URL"):
            assert config.base_url + HomePageContent.URL == page.url

        # 3. Do Title verification
        with allure.step("Verify web page title"):
            assert HomePageContent.TITLE == page.title

        # 4. Type username
        with allure.step("Type username"):
            page.customer_login.enter_username(user.username)

        # 4. Type password
        with allure.step("Type password"):
            page.customer_login.enter_password(user.password)

        # 5. Hit "Log In" button
        with allure.step("Hit \"Log In\" button"):
            page = page.customer_login.hit_login_button()

        # 6. Verify "Welcome" message
        with allure.step("Verify \"Welcome\" message"):
            assert "Welcome {} {}".format(user.first_name, user.last_name) == page.account_services_menu.welcome_message

        # 7. Verify that "Account Services" menu title is present
        with allure.step("Verify that \"Account Services\" menu title is present"):
            assert "Account Services" == page.account_services_menu.menu_title

        # 8. Do URL verification
        with allure.step("Do URL verification"):
            assert config.base_url + AccountsOverviewPageContent.URL == page.url

        # 9. Log Out
        with allure.step("Log Out"):
            page = page.account_services_menu.hit_log_out_button()

        # 10. Do URL verification
        with allure.step("Do URL verification"):
            assert config.base_url + HomePageContent.URL == page.url

        # 11. Verify that "Account Services" menu is not present
        with allure.step("Verify that \"Account Services\" menu is not present"):
            with pytest.raises(NoSuchElementException):
                AccountServicesMenuModel(config=config,
                                         driver=self.driver,
                                         explicit_wait_time=10).menu_title()

        # 12. Verify web page title
        with allure.step("Verify web page title"):
            assert HomePageContent.TITLE == page.title

        # 13. Close web browser
        with allure.step("Close web browser"):
            page.close()

