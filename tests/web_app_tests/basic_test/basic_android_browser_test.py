"""Basic Web App Test Case"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.web_app_tests.android_browser_base_testcase import AndroidBrowserBaseTestCase


@allure.epic('Android Web App')
@allure.parent_suite('End To End')
@allure.suite("Web App Test Suite")
@allure.sub_suite("Positive Tests")
@allure.feature("Basic Functionality")
@allure.story('Basic Elements')
class TestBasicAndroidBrowserCase(AndroidBrowserBaseTestCase):
    """
    Test basic web app functionality
    """

    def test_open_google_search(self):
        """
        Open web browser on Google search page
        Type "Hello Appium"
        Hit Search button
        Close web page
        :return:
        """

        allure.dynamic.title("Basic web app test")
        allure.dynamic.severity(allure.severity_level.MINOR)

        # Open Google search web page
        self.page.get("http://google.com")
        WebDriverWait(self.page, 5).until(EC.title_contains("Google"))
        current_url = self.page.current_url

        # Type "Hello Appium" in search field
        search_field = self.page.find_element(By.NAME, 'q')
        search_field.send_keys("Hello Appium")

        # Hit search button
        search_btn = self.page.find_element(By.XPATH,
                                            '//*[@id="tsf"]/div[2]/div[1]/div[1]/button[2]')
        search_btn.click()

        # Wait until search results appears
        WebDriverWait(self.page, 5).until(EC.url_changes(current_url))

        # Verify web page title
        assert "Hello Appium - Google Search" == self.page.title
