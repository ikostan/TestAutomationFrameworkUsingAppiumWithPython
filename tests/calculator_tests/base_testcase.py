"""Base Test Case"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


import os
import unittest


import allure
from allure_commons.types import AttachmentType

from page_objects.calculator_page_model import CalculatorPageModel
from utils.driver import Driver

from selenium.common.exceptions import TimeoutException


class BaseTestCase(unittest.TestCase):
    """
    Base Test Case
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

    def clear_calculator_screen(self):
        """
        Clear screen output
        :return:
        """
        with allure.step("Clear screen output."):
            print('\nClear screen output.')

            is_screen_clear = False
            while not is_screen_clear:

                is_screen_clear = True

                try:
                    self.app.del_btn.tap()
                except TimeoutException:
                    self.app.clr.tap()

                if self.app.screen_formula:
                    if self.app.screen_formula.label != '':
                        is_screen_clear = False
                        continue

                if self.app.screen_result:
                    if self.app.screen_result.label != '':
                        is_screen_clear = False
                        continue

    def scientific_notation_to_integer_converter(self, data) -> str:
        """
        Convert scientific notation (string like '1e7') to an integer:
            In Python the e-form indicates a float, as does the presence of a
            decimal point, but you can convert to float and then to int: int(float('1e7')) >>> 10000000

        Source: https://mail.python.org/pipermail/python-list/2009-November/557390.html

        Example:
            1e5 is a number expressed using scientific notation and it means
            10 to the 5th power (the e meaning 'exponent'), so 1e5 is equal to 100000,
            both notations are interchangeably meaning the same.

        Source: https://stackoverflow.com/questions/26174531/what-is-the-meaning-of-number-1e5
        :param data:
        :return:
        """
        if 'E' not in data:
            return data
        else:
            print("Converting {} into int.".format(data))
            return str(int(float(self.app.screen_result.label.replace('.E', 'e'))))

    def perform_addition(self, args):
        """
        Perform addition action for any list of numbers.
        :param args:
        :return:
        """
        self.clear_calculator_screen()

        with allure.step("Performing addition of following numbers: {}".format(args)):
            print("\nPerforming addition of following numbers: {}".format(args))

            for i, arg in enumerate(args):

                if arg < 0:
                    self.app.minus.tap()

                if len(str(arg)) == 1:
                    self.app.digits[abs(arg)].tap()
                else:
                    for char in str(arg):

                        if char.isdigit():
                            self.app.digits[int(char)].tap()

                        if char == '.':
                            self.app.dot.tap()

                if i != len(args) - 1:
                    self.app.plus.tap()

            print("Formula: {}".format(self.app.screen_formula.label))
            print("Result: {}".format(self.app.screen_result.label))

            with allure.step("Perform result (screen) evaluation: "
                             "{} should be equal {}".format(self.app.screen_result.label,
                                                            eval(self.app.screen_formula.label))):

                expected = str(eval(self.app.screen_formula.label))
                actual = self.scientific_notation_to_integer_converter(self.app.screen_result.label)
                assert expected == actual

            self.app.equal.tap()
            print("Screen output: {}".format(self.app.screen_result.label))

