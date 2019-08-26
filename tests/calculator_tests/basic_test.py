"""Basic calculator_test Test Case"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import os
import unittest

from selenium.common.exceptions import TimeoutException

import allure
from allure_commons.types import AttachmentType

from page_objects.calculatoe_page_model import CalculatorPageModel
from utils.driver import Driver


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
        with allure.step("Set driver to None"):
            cls._driver = None

    @classmethod
    def tearDownClass(cls) -> None:
        with allure.step("Close Page Model > Set driver to None"):
            if cls._driver:
                if cls._driver.driver_instance:
                    cls._driver.driver_instance.quit()
                cls._driver = None

    def setUp(self) -> None:
        with allure.step("Set up driver object"):
            self._driver = Driver()
            self._driver.set_capability("appPackage", "com.android.calculator2")
            self._driver.set_capability("appActivity", "com.android.calculator2.Calculator")

        with allure.step("Set up Page Model object"):
            self.app = CalculatorPageModel(self._driver.driver_instance)

        # Set the current device/browser orientation
        # self.driver.driver_instance.orientation = "LANDSCAPE"

        # NOTE: In addCleanup, the first in, is executed last.
        with allure.step("Set up Cleanup methods"):
            self.addCleanup(self._driver.driver_instance.quit)
            self.addCleanup(self.screen_shot)
            self._driver.driver_instance.implicitly_wait(3)

    def screen_shot(self):
        """
        Take a Screen-shot of the drive homepage, when it Failed.
        Source: https://stackoverflow.com/questions/12024848/automatic-screenshots-when-test-fail-by-selenium-webdriver-in-python
        """
        for error in self._outcome.errors:
            if error:
                file_name = "screenshot_{}.png".format(self.id())
                self._driver.driver_instance.get_screenshot_as_file(file_name)
                allure.attach.file('./' + file_name, attachment_type=AttachmentType.PNG)
                os.remove('./' + file_name)

    def test_btn_visibility(self):
        """
        Test basic functionality:

        Should be able to open calculator_test app
        Should be able to close the app
        Check for the visibility of all buttons (0-9, DEL, CLR, ., +, -, *, /, =)
        """

        allure.dynamic.title("Buttons visibility test")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        # Digits 0-9
        with allure.step("Test 0-9 digits/buttons visibility"):
            '''
            for key in CalculatorPageLocator.DIGITS:
                assert BaseElement(self.driver.driver_instance,
                                   CalculatorPageLocator.DIGITS[key]).is_visible
            '''
            for btn in self.app.buttons:
                assert btn.is_visible

        # . button
        with allure.step("Test '.' button visibility"):
            '''
            btn = WebDriverWait(self.driver.driver_instance, 5).until(
                EC.presence_of_element_located(CalculatorPageLocator.POINT_BTN))
            assert btn.is_displayed()
            
            assert BaseElement(self.driver.driver_instance,
                               CalculatorPageLocator.POINT_BTN).is_visible
            '''
            assert self.app.dot.is_visible

        # +
        with allure.step("Test '+' button visibility"):
            '''
            btn = WebDriverWait(self.driver.driver_instance, 5).until(
                EC.presence_of_element_located(CalculatorPageLocator.PLUS_BTN))
            assert btn.is_displayed()
            
            assert BaseElement(self.driver.driver_instance,
                               CalculatorPageLocator.PLUS_BTN).is_visible
            '''
            assert self.app.plus.is_visible

        # -
        with allure.step("Test '-' button visibility"):
            '''
            btn = WebDriverWait(self.driver.driver_instance, 5).until(
                EC.presence_of_element_located(CalculatorPageLocator.MINUS_BTN))
            assert btn.is_displayed()
            
            assert BaseElement(self.driver.driver_instance,
                               CalculatorPageLocator.MINUS_BTN).is_visible
            '''
            assert self.app.minus.is_visible

        # *
        with allure.step("Test '*' button visibility"):
            '''
            btn = WebDriverWait(self.driver.driver_instance, 5).until(
                EC.presence_of_element_located(CalculatorPageLocator.MULTIPLICATION_BTN))
            assert btn.is_displayed()

            assert BaseElement(self.driver.driver_instance,
                               CalculatorPageLocator.MULTIPLICATION_BTN).is_visible
            '''
            assert self.app.multiplication.is_visible

        # /
        with allure.step("Test '/' button visibility"):
            '''
            btn = WebDriverWait(self.driver.driver_instance, 5).until(
                EC.presence_of_element_located(CalculatorPageLocator.DIVISION_BTN))
            assert btn.is_displayed()

            assert BaseElement(self.driver.driver_instance,
                               CalculatorPageLocator.DIVISION_BTN).is_visible
            '''
            assert self.app.division.is_visible

        # DEL
        with allure.step("Test 'DEL' button visibility"):
            '''
            btn = WebDriverWait(self.driver.driver_instance, 5).until(
                EC.presence_of_element_located(CalculatorPageLocator.DEL_BTN))
            assert btn.is_displayed()
            
            assert BaseElement(self.driver.driver_instance,
                               CalculatorPageLocator.DEL_BTN).is_visible
            '''
            assert self.app.del_btn.is_visible

        # CLR button is not presented by default
        with allure.step("Test 'CLR' button visibility"):
            '''
            with self.assertRaises(TimeoutException):
                WebDriverWait(self.driver.driver_instance, 5).until(
                    EC.presence_of_element_located(CalculatorPageLocator.CLEAR_BTN))
            
            with self.assertRaises(TimeoutException):
                BaseElement(self.driver.driver_instance,
                            CalculatorPageLocator.CLEAR_BTN)
            '''
            with self.assertRaises(TimeoutException):
                visibility_status = self.app.clr.is_visible

        # =
        with allure.step("Test '=' button visibility"):
            '''
            btn = WebDriverWait(self.driver.driver_instance, 5).until(
                EC.presence_of_element_located(CalculatorPageLocator.EQUAL_BTN))
            assert btn.is_displayed()
            
            assert BaseElement(self.driver.driver_instance,
                               CalculatorPageLocator.EQUAL_BTN).is_visible
            '''
            assert self.app.equal.is_visible

        # Display
        with allure.step("Test main display visibility"):
            '''
            btn = WebDriverWait(self.driver.driver_instance, 5).until(
                EC.presence_of_element_located(CalculatorPageLocator.DISPLAY))
            assert btn.is_displayed()
            
            assert BaseElement(self.driver.driver_instance,
                               CalculatorPageLocator.DISPLAY).is_visible
            '''
            assert self.app.main_screen.is_visible

    def test_entering_digits(self):
        """
        Should be able to open calculator_test app
        Should be able to enter digits
        Should be able to see input/output
        Should be able to close the app
        :return:
        """

        allure.dynamic.title("0-9 buttons basic functionality test")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Enter digits 0-9"):
            '''
            for key in CalculatorPageLocator.DIGITS:
                btn = WebDriverWait(self.driver.driver_instance, 5).until(
                    EC.element_to_be_clickable(CalculatorPageLocator.DIGITS[key]))
                btn.click()
            '''
            for digit in self.app.digits:
                digit.tap()

        with allure.step("Verify screen output"):
            '''
            screen_formula = WebDriverWait(self.driver.driver_instance, 5).until(
                EC.presence_of_element_located(CalculatorPageLocator.SCREEN_FORMULA))
            assert screen_formula.text == '0123456789'
            '''
            assert self.app.screen_formula.label == '0123456789'

    def test_equal_btn(self):
        """
        Should be able to open calculator_test app
        Should be able to enter digits
        Should be able to use "=" button
        Should be able to see input/output
        Should be able to close the app
        :return:
        """

        allure.dynamic.title("'=' basic functionality test")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Enter digits 0-9"):
            '''
            for key in CalculatorPageLocator.DIGITS:
                btn = WebDriverWait(self.driver.driver_instance, 5).until(
                    EC.element_to_be_clickable(CalculatorPageLocator.DIGITS[key]))
                btn.click()
            '''
            for digit in self.app.digits:
                digit.tap()

        with allure.step("Press '=' button"):
            '''
            btn = WebDriverWait(self.driver.driver_instance, 5).until(
                EC.element_to_be_clickable(CalculatorPageLocator.EQUAL_BTN))
            btn.click()
            '''
            self.app.equal.tap()

        with allure.step("Verify screen output"):
            '''
            screen_result = WebDriverWait(self.driver.driver_instance, 5).until(
                EC.presence_of_element_located(CalculatorPageLocator.SCREEN_RESULT))
            assert screen_result.text == '123456789'
            '''
            assert self.app.screen_result.label == '123456789'

    def test_clear_btn(self):
        """
        Should be able to open calculator_test app
        Should be able to use "CLR" button
        Should be able to close the app
        :return:
        """

        allure.dynamic.title("'CLR' basic functionality test")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Enter digits 0-9"):
            '''
            for key in CalculatorPageLocator.DIGITS:
                btn = WebDriverWait(self.driver.driver_instance, 5).until(
                    EC.element_to_be_clickable(CalculatorPageLocator.DIGITS[key]))
                btn.click()
            '''
            for digit in self.app.digits:
                digit.tap()

        with allure.step("Press '=' button"):
            '''
            btn = WebDriverWait(self.driver.driver_instance, 5).until(
                EC.element_to_be_clickable(CalculatorPageLocator.EQUAL_BTN))
            btn.click()
            '''
            self.app.equal.tap()

        with allure.step("Test 'CLR' button visibility"):
            '''
            btn = WebDriverWait(self.driver.driver_instance, 5).until(
                EC.presence_of_element_located(CalculatorPageLocator.CLEAR_BTN))
            assert btn.is_displayed()
            '''
            assert self.app.clr.is_visible

        with allure.step("Press 'CLR' button"):
            '''
            btn = WebDriverWait(self.driver.driver_instance, 5).until(
                EC.element_to_be_clickable(CalculatorPageLocator.CLEAR_BTN))
            btn.click()
            '''
            self.app.clr.tap()

        with allure.step("Verify formula screen output"):
            '''
            screen_formula = WebDriverWait(self.driver.driver_instance, 5).until(
                EC.presence_of_element_located(CalculatorPageLocator.SCREEN_FORMULA))
            assert screen_formula.text == ''
            '''
            assert self.app.screen_formula.label == ''

        with allure.step("Verify result screen output"):
            '''
            screen_result = WebDriverWait(self.driver.driver_instance, 5).until(
                EC.presence_of_element_located(CalculatorPageLocator.SCREEN_RESULT))
            assert screen_result.text == ''
            '''
            assert self.app.screen_result.label == ''

    def test_delete_btn(self):
        """
        Should be able to open calculator_test app
        Should be able to enter digits
        Should be able to use "DEL" button
        Should be able to see input/output
        Should be able to close the app
        :return:
        """

        allure.dynamic.title("'DEL' basic functionality test")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Enter digits 0-9"):
            '''
            for key in CalculatorPageLocator.DIGITS:
                btn = WebDriverWait(self.driver.driver_instance, 5).until(
                    EC.element_to_be_clickable(CalculatorPageLocator.DIGITS[key]))
                btn.click()
            '''
            for digit in self.app.digits:
                digit.tap()

        with allure.step("Test 'DEL' button"):

            for index in range(len('0123456789')):
                with allure.step("Press 'DEL' button"):
                    '''
                    btn = WebDriverWait(self.driver.driver_instance, 5).until(
                        EC.element_to_be_clickable(CalculatorPageLocator.DEL_BTN))
                    btn.click()
                    '''
                    self.app.del_btn.tap()

                with allure.step("Verify formula screen output"):
                    '''
                    screen_formula = WebDriverWait(self.driver.driver_instance, 5).until(
                        EC.presence_of_element_located(CalculatorPageLocator.SCREEN_FORMULA))
                    assert screen_formula.text == '0123456789'[0:len('0123456789') - (1 + index)]
                    '''
                    assert self.app.screen_formula.label == '0123456789'[0:len('0123456789') - (1 + index)]

        with allure.step("Verify formula screen output"):
            '''
            screen_formula = WebDriverWait(self.driver.driver_instance, 5).until(
                EC.presence_of_element_located(CalculatorPageLocator.SCREEN_FORMULA))
            assert screen_formula.text == ''
            '''
            assert self.app.screen_formula.label == ''

        with allure.step("Verify result screen output"):
            '''
            screen_result = WebDriverWait(self.driver.driver_instance, 5).until(
                EC.presence_of_element_located(CalculatorPageLocator.SCREEN_RESULT))
            assert screen_result.text == ''
            '''
            assert self.app.screen_result.label == ''
