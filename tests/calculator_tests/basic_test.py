"""Basic calculator_test Test Case"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import os
import unittest

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import allure
from allure_commons.types import AttachmentType

from utils.driver import Driver
from locators.page_locator import PageLocator


@allure.epic('Android Native App')
@allure.parent_suite('End To End')
@allure.suite("calculator_test Test Suite")
@allure.sub_suite("Positive Tests")
@allure.feature("Basic Functionality")
@allure.story('Basic Buttons')
class TestBasicCalculatorCases(unittest.TestCase):
    """
    Test basic functionality:

    Should be able to open calculator_test app
    Should be able to enter digits
    Should be able to use "=" button
    Should be able to use "DEL" button
    Should be able to use "CLR" button
    Should be able to see input/output
    Should be able to close the app
    Check for the visibility of all buttons (0-9, DEL, CLR, . +,-,*,/,=)
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = None

    @classmethod
    def tearDownClass(cls) -> None:
        if cls.driver:
            if cls.driver.instance:
                cls.driver.instance.quit()
            cls.driver = None

    def setUp(self) -> None:
        self.driver = Driver()
        # NOTE: In addCleanup, the first in, is executed last.
        self.addCleanup(self.driver.instance.quit)
        self.addCleanup(self.screen_shot)
        self.driver.instance.implicitly_wait(3)

    def screen_shot(self):
        """
        Take a Screen-shot of the drive homepage, when it Failed.
        Source: https://stackoverflow.com/questions/12024848/automatic-screenshots-when-test-fail-by-selenium-webdriver-in-python
        """
        for error in self._outcome.errors:
            if error:
                file_name = "screenshot_{}.png".format(self.id())
                self.driver.instance.get_screenshot_as_file(file_name)
                allure.attach.file('./' + file_name, attachment_type=AttachmentType.PNG)
                os.remove('./' + file_name)

    def test_btn_visibility(self):
        """
        Test basic functionality:

        Should be able to open calculator_test app
        Should be able to close the app
        Check for the visibility of all buttons (0-9, DEL, CLR, ., +, -, *, /, =)
        """

        # Digits 0-9
        for key in PageLocator.DIGITS:
            btn = WebDriverWait(self.driver.instance, 5).until(
                EC.presence_of_element_located(PageLocator.DIGITS[key]))
            assert btn.is_displayed()

        # . button
        btn = WebDriverWait(self.driver.instance, 5).until(
            EC.presence_of_element_located(PageLocator.POINT_BTN))
        assert btn.is_displayed()

        # +
        btn = WebDriverWait(self.driver.instance, 5).until(
            EC.presence_of_element_located(PageLocator.PLUS_BTN))
        assert btn.is_displayed()

        # -
        btn = WebDriverWait(self.driver.instance, 5).until(
            EC.presence_of_element_located(PageLocator.MINUS_BTN))
        assert btn.is_displayed()

        # *
        btn = WebDriverWait(self.driver.instance, 5).until(
            EC.presence_of_element_located(PageLocator.MULTIPLICATION_BTN))
        assert btn.is_displayed()

        # /
        btn = WebDriverWait(self.driver.instance, 5).until(
            EC.presence_of_element_located(PageLocator.DIVISION_BTN))
        assert btn.is_displayed()

        # DEL
        btn = WebDriverWait(self.driver.instance, 5).until(
            EC.presence_of_element_located(PageLocator.DEL_BTN))
        assert btn.is_displayed()

        # CLR button is not presented by default
        with self.assertRaises(TimeoutException):
            WebDriverWait(self.driver.instance, 5).until(
                EC.presence_of_element_located(PageLocator.CLEAR_BTN))

        # =
        btn = WebDriverWait(self.driver.instance, 5).until(
            EC.presence_of_element_located(PageLocator.EQUAL_BTN))
        assert btn.is_displayed()

        # Display
        btn = WebDriverWait(self.driver.instance, 5).until(
            EC.presence_of_element_located(PageLocator.DISPLAY))
        assert btn.is_displayed()

    def test_entering_digits(self):
        """
        Should be able to open calculator_test app
        Should be able to enter digits
        Should be able to see input/output
        Should be able to close the app
        :return:
        """

        for key in PageLocator.DIGITS:
            btn = WebDriverWait(self.driver.instance, 5).until(
                EC.element_to_be_clickable(PageLocator.DIGITS[key]))
            btn.click()

        screen_formula = WebDriverWait(self.driver.instance, 5).until(
            EC.presence_of_element_located(PageLocator.SCREEN_FORMULA))
        assert screen_formula.text == '0123456789'

    def test_equal_btn(self):
        """
        Should be able to open calculator_test app
        Should be able to enter digits
        Should be able to use "=" button
        Should be able to see input/output
        Should be able to close the app
        :return:
        """

        for key in PageLocator.DIGITS:
            btn = WebDriverWait(self.driver.instance, 5).until(
                EC.element_to_be_clickable(PageLocator.DIGITS[key]))
            btn.click()

        btn = WebDriverWait(self.driver.instance, 5).until(
            EC.element_to_be_clickable(PageLocator.EQUAL_BTN))
        btn.click()

        screen_result = WebDriverWait(self.driver.instance, 5).until(
            EC.presence_of_element_located(PageLocator.SCREEN_RESULT))
        assert screen_result.text == '123456789'

    def test_clear_btn(self):
        """
        Should be able to open calculator_test app
        Should be able to use "CLR" button
        Should be able to close the app
        :return:
        """

        for key in PageLocator.DIGITS:
            btn = WebDriverWait(self.driver.instance, 5).until(
                EC.element_to_be_clickable(PageLocator.DIGITS[key]))
            btn.click()

        btn = WebDriverWait(self.driver.instance, 5).until(
            EC.element_to_be_clickable(PageLocator.EQUAL_BTN))
        btn.click()

        btn = WebDriverWait(self.driver.instance, 5).until(
            EC.presence_of_element_located(PageLocator.CLEAR_BTN))
        assert btn.is_displayed()

        btn = WebDriverWait(self.driver.instance, 5).until(
            EC.element_to_be_clickable(PageLocator.CLEAR_BTN))
        btn.click()

        screen_formula = WebDriverWait(self.driver.instance, 5).until(
            EC.presence_of_element_located(PageLocator.SCREEN_FORMULA))
        assert screen_formula.text == ''

        screen_result = WebDriverWait(self.driver.instance, 5).until(
            EC.presence_of_element_located(PageLocator.SCREEN_RESULT))
        assert screen_result.text == ''

    def test_delete_btn(self):
        """
        Should be able to open calculator_test app
        Should be able to enter digits
        Should be able to use "DEL" button
        Should be able to see input/output
        Should be able to close the app
        :return:
        """

        for key in PageLocator.DIGITS:
            btn = WebDriverWait(self.driver.instance, 5).until(
                EC.element_to_be_clickable(PageLocator.DIGITS[key]))
            btn.click()

        for index in range(len('0123456789')):
            btn = WebDriverWait(self.driver.instance, 5).until(
                EC.element_to_be_clickable(PageLocator.DEL_BTN))
            btn.click()

            screen_formula = WebDriverWait(self.driver.instance, 5).until(
                EC.presence_of_element_located(PageLocator.SCREEN_FORMULA))
            assert screen_formula.text == '0123456789'[0:len('0123456789') - (1 + index)]

        screen_formula = WebDriverWait(self.driver.instance, 5).until(
            EC.presence_of_element_located(PageLocator.SCREEN_FORMULA))
        assert screen_formula.text == ''

        screen_result = WebDriverWait(self.driver.instance, 5).until(
            EC.presence_of_element_located(PageLocator.SCREEN_RESULT))
        assert screen_result.text == ''
