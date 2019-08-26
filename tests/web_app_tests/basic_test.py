"""Basic Web App Test Case"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import os
import unittest

import allure
from allure_commons.types import AttachmentType

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver import Driver


@allure.epic('Android Web App')
@allure.parent_suite('End To End')
@allure.suite("Web App Test Suite")
@allure.sub_suite("Positive Tests")
@allure.feature("Basic Functionality")
@allure.story('Basic Elements')
class TestBasicCalculatorCases(unittest.TestCase):
    """
    Test basic web app functionality
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = None

    @classmethod
    def tearDownClass(cls) -> None:
        if cls.driver:
            if cls.driver.driver_instance:
                cls.driver.driver_instance.quit()
            cls.driver = None

    def setUp(self) -> None:
        self.driver = Driver()
        self.driver.set_capability("browserName", "Chrome")
        self.driver.set_capability('chromedriverExecutable',
                                   'C:\\Users\\superadmin\\Documents\\GitHub\\'
                                   'TEST_AUTOMATION_FRAMEWORK_USING_APPIUM_WITH_PYTHON\\'
                                   'drivers\\chromedriver\\v2_44\\chromedriver.exe')

        # NOTE: In addCleanup, the first in, is executed last.
        self.addCleanup(self.driver.driver_instance.quit)
        self.addCleanup(self.screen_shot)
        self.driver.driver_instance.implicitly_wait(3)

    def screen_shot(self):
        """
        Take a Screen-shot of the drive homepage, when it Failed.
        Source: https://stackoverflow.com/questions/12024848/automatic-screenshots-when-test-fail-by-selenium-webdriver-in-python
        """
        for error in self._outcome.errors:
            if error:
                file_name = "screenshot_{}.png".format(self.id())
                self.driver.driver_instance.get_screenshot_as_file(file_name)
                allure.attach.file('./' + file_name, attachment_type=AttachmentType.PNG)
                os.remove('./' + file_name)

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
        self.driver.driver_instance.get("http://google.com")
        WebDriverWait(self.driver.driver_instance, 5).until(EC.title_contains("Google"))
        current_url = self.driver.driver_instance.current_url

        # Type "Hello Appium" in search field
        search_field = self.driver.driver_instance.find_element(By.NAME, 'q')
        search_field.send_keys("Hello Appium")

        # Hit search button
        search_btn = self.driver.driver_instance.find_element(By.XPATH,
                                                              '//*[@id="tsf"]/div[2]/div[1]/div[1]/button[2]')
        search_btn.click()

        # Wait until search results appears
        WebDriverWait(self.driver.driver_instance, 5).until(EC.url_changes(current_url))

        # Verify web page title
        assert "Hello Appium - Google Search" == self.driver.driver_instance.title
