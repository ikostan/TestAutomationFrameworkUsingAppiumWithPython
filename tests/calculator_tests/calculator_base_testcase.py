"""Base Test Case"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


import os
import unittest

import allure
from allure_commons.types import AttachmentType

from appium.webdriver.appium_service import AppiumService

from page_objects.calculator_page_model import CalculatorPageModel
from utils.driver import Driver

from selenium.common.exceptions import TimeoutException


class CalculatorBaseTestCase(unittest.TestCase):
    """
    Base Test Case
    """

    @classmethod
    def setUpClass(cls) -> None:
        with allure.step("Start Appium Service"):
            # Python client actually comes with a handy module called AppiumService
            # that you can use to programmatically start/stop an Appium server.
            # Source: https://stackoverflow.com/questions/51734382/how-to-start-appium-server-programmatically-in-python
            # Source: https://github.com/appium/python-client/blob/master/appium/webdriver/appium_service.py

            # cls._appium_service = AppiumService()
            # cls._appium_service.start()
            os.system("start /B start cmd.exe @cmd /k appium")

        with allure.step("Set driver to None"):
            cls._driver = None

    @classmethod
    def tearDownClass(cls) -> None:
        with allure.step("Close Page Model > Set driver to None"):
            if cls._driver:
                if cls._driver.driver_instance:
                    cls._driver.driver_instance.quit()
                cls._driver = None

        with allure.step("Stop Appium Service"):
            # Stop Appium service
            # Source: https://discuss.appium.io/t/launching-and-stopping-appium-server-programmtically/700/2
            if cls._appium_service:
                # cls.appium_service.stop()
                os.system('taskkill /F /IM node.exe')

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

    def enter_number(self, number):
        """
        Enter a number
        :param number:
        :return:
        """

        print("Enter a number: {}".format(number))

        if number < 0:
            self.app.minus.tap()

        if len(str(number)) == 1:
            self.app.digits[abs(number)].tap()
        else:
            for char in str(number):

                if char.isdigit():
                    self.app.digits[int(char)].tap()

                if char == '.':
                    self.app.dot.tap()

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

    @staticmethod
    def eval_formula(data) -> str:
        """
        Converts input to a string if needed
        Check if the eval result as a string == float, and if so process it as an integer
        Convert result to a string and return it
        :return:
        """

        if not isinstance(data, str):
            data = str(data)

        expected = eval(data)
        expected_int = int(expected)

        if expected == float(expected_int):
            print("Evaluation formula result: {}".format(expected_int))
            return str(expected_int)
        else:
            print("Evaluation formula result: {}".format(expected))
            return str(expected)

    def perform_subtraction(self, args):
        """
        Perform subtraction for any list of numbers.
        :param args:
        :return:
        """
        self.clear_calculator_screen()

        with allure.step("Performing subtraction of following numbers: {}".format(args)):
            print("\nPerforming subtraction of following numbers: {}".format(args))

            for i, arg in enumerate(args):

                self.enter_number(arg)

                if i != len(args) - 1:
                    self.app.minus.tap()

            print("Formula: {}".format(self.app.screen_formula.label))
            print("Result: {}".format(self.app.screen_result.label))

            expected = self.eval_formula(self.app.screen_formula.label)
            actual = self.app.screen_result.label
            with allure.step("Perform result (screen) evaluation: "
                             "{} should be equal {}".format(actual, expected)):
                print('Perform result (screen) evaluation: '
                      '{} should be equal {}'.format(actual, expected))
                assert expected == actual

            self.app.equal.tap()
            print("Screen output: {}".format(self.app.screen_result.label))

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

                self.enter_number(arg)

                if i != len(args) - 1:
                    self.app.plus.tap()

            print("Formula: {}".format(self.app.screen_formula.label))
            print("Result: {}".format(self.app.screen_result.label))

            expected = self.eval_formula(self.app.screen_formula.label)
            actual = self.app.screen_result.label
            with allure.step("Perform result (screen) evaluation: "
                             "{} should be equal {}".format(actual, expected)):
                print('Perform result (screen) evaluation: '
                      '{} should be equal {}'.format(actual, expected))
                assert expected == actual

            self.app.equal.tap()
            print("Screen output: {}".format(self.app.screen_result.label))
