"""Android Calculator App Test: Base Test Case"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import os
import unittest

import allure
from allure_commons.types import AttachmentType

from page_object_models.calculator.calculator_page_model import CalculatorPageModel
from utils.driver import Driver

from selenium.common.exceptions import TimeoutException

from utils.get_args_from_cli import get_args


class AndroidCalculatorBaseTestCase(unittest.TestCase):
    """
    Android Calculator App Test: Base Test Case
    """

    @classmethod
    def setUpClass(cls) -> None:

        with allure.step("Get args from CLI"):
            cls.args = get_args()

        with allure.step("Start Appium Service"):
            # that you can use to programmatically start/stop an Appium server.
            # Source: https://stackoverflow.com/questions/51734382/how-to-start-appium-server-programmatically-in-python
            # Source: https://github.com/appium/python-client/blob/master/appium/webdriver/appium_service.py
            # Source: https://discuss.appium.io/t/launching-and-stopping-appium-server-programmtically/700/2
            os.system("start /B start cmd.exe @cmd /k appium --relaxed-security")

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
            # Stop Appium Service
            # Source: https://discuss.appium.io/t/launching-and-stopping-appium-server-programmtically/700/2
            os.system('taskkill /F /IM node.exe')

    def setUp(self) -> None:

        with allure.step("Set up driver object"):
            self._driver = Driver()

            # Add desired capabilities:

            for key in self.args:
                self._driver.set_capability(key, self.args[key])

            '''
            self._driver.set_capability("platformName",
                                        "android")

            self._driver.set_capability("deviceName",
                                        "Android Tablet")

            self._driver.set_capability("automationName",
                                        "Appium")

            self._driver.set_capability("appPackage",
                                        "com.android.calculator2")

            self._driver.set_capability("appActivity",
                                        "com.android.calculator2.Calculator")
            '''
            self._driver.set_capability('chromedriverExecutable',
                                        'C:\\Users\\superadmin\\Documents\\GitHub\\'
                                        'TEST_AUTOMATION_FRAMEWORK_USING_APPIUM_WITH_PYTHON\\'
                                        'drivers\\chromedriver\\v2_44\\chromedriver.exe')

        with allure.step("Set up Page Model object"):
            self.app = CalculatorPageModel(self._driver.driver_instance)

        # NOTE: In addCleanup, the first in, is executed last.
        with allure.step("Set up Cleanup methods"):
            self.addCleanup(self._driver.driver_instance.quit)
            self.addCleanup(self.snap_shot)
            self._driver.driver_instance.implicitly_wait(3)

    def enter_digit(self, number):
        """
        Enter a number
        :param number:
        :return:
        """
        print("Enter a number: {}".format(number))

        if not isinstance(number, str):
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

    def snap_shot(self):
        """
        Take a Screen-shot + Appium Server Log
        """
        for error in self._outcome.errors:
            if error:

                # Screen shot:
                # Source: https://stackoverflow.com/questions/12024848/
                # automatic-screenshots-when-test-fail-by-selenium-webdriver-in-python

                file_name = "screenshot_{}.png".format(self.id())
                self._driver.driver_instance.get_screenshot_as_file(file_name)
                allure.attach.file('./' + file_name, attachment_type=AttachmentType.PNG)
                os.remove(file_name)

                # Get Appium Server Logs:
                # Source: https://appium.readthedocs.io/en/stable/en/commands/session/logs/get-log/#get-logs

                appium_server_log = self._driver.driver_instance.get_log('server')
                file_name = "./appium_server_log.txt"
                with open(file_name, "w", encoding="utf-8") as f:
                    for dictionary in appium_server_log:
                        for k in dictionary:
                            f.write("{} : {}\n".format(k, dictionary[k]))
                        f.write("\n")

                allure.attach.file(file_name, attachment_type=AttachmentType.TEXT)
                os.remove(file_name)

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
                    if self.app.screen_formula.formatted_text != '':
                        is_screen_clear = False
                        continue

                if self.app.screen_result:
                    if self.app.screen_result.formatted_text != '':
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
        Perform subtraction calculation for any list of numbers.
        :param args:
        :return:
        """
        self.clear_calculator_screen()

        with allure.step("Performing subtraction calculation of following numbers: {}".format(args)):
            print("\nPerforming subtraction calculation of following numbers: {}".format(args))

            for i, arg in enumerate(args):

                self.enter_digit(arg)

                if i != len(args) - 1:
                    self.app.minus.tap()

            print("Formula: {}".format(self.app.screen_formula.formatted_text))
            print("Result: {}".format(self.app.screen_result.formatted_text))

            expected = self.eval_formula(self.app.screen_formula.formatted_text)
            actual = self.app.screen_result.formatted_text
            with allure.step("Perform result (screen) evaluation: "
                             "{} should be equal {}".format(actual, expected)):
                print('Perform result (screen) evaluation: '
                      '{} should be equal {}'.format(actual, expected))
                assert expected == actual

            self.app.equal.tap()
            print("Screen output: {}".format(self.app.screen_result.formatted_text))

    def perform_addition(self, args):
        """
        Perform addition calculation for any list of numbers.
        :param args:
        :return:
        """
        self.clear_calculator_screen()

        with allure.step("Performing addition calculation of following numbers: {}".format(args)):
            print("\nPerforming addition calculation of following numbers: {}".format(args))

            for i, arg in enumerate(args):

                self.enter_digit(arg)

                if i != len(args) - 1:
                    self.app.plus.tap()

            print("Formula: {}".format(self.app.screen_formula.formatted_text))
            print("Result: {}".format(self.app.screen_result.formatted_text))

            expected = self.eval_formula(self.app.screen_formula.formatted_text)
            actual = self.app.screen_result.formatted_text
            with allure.step("Perform result (screen) evaluation: "
                             "{} should be equal {}".format(actual, expected)):
                print('Perform result (screen) evaluation: '
                      '{} should be equal {}'.format(actual, expected))
                assert expected == actual

            self.app.equal.tap()
            print("Screen output: {}".format(self.app.screen_result.formatted_text))

    def perform_multiplication(self, args):
        """
        Perform multiplication calculation for any list of numbers.
        :param args:
        :return:
        """
        self.clear_calculator_screen()

        with allure.step("Performing multiplication calculation of following numbers: {}".format(args)):
            print("\nPerforming multiplication calculation of following numbers: {}".format(args))

            for i, arg in enumerate(args):

                self.enter_digit(arg)

                if i != len(args) - 1:
                    self.app.multiplication.tap()

            print("Formula: {}".format(self.app.screen_formula.formatted_text))
            print("Result: {}".format(self.app.screen_result.formatted_text))

            expected = self.eval_formula(self.app.screen_formula.formatted_text)
            actual = self.app.screen_result.formatted_text
            with allure.step("Perform result (screen) evaluation: "
                             "{} should be equal {}".format(actual, expected)):
                print('Perform result (screen) evaluation: '
                      '{} should be equal {}'.format(actual, expected))
                if '.' in expected:
                    if len(expected[expected.index('.'):]) > 12:
                        assert '%.13f'.format(expected) == '%.13f'.format(actual)
                    else:
                        assert expected == actual

            self.app.equal.tap()
            print("Screen output: {}".format(self.app.screen_result.formatted_text))

    def perform_division(self, args):
        """
        Perform division calculation for any list of numbers.
        :param args:
        :return:
        """
        self.clear_calculator_screen()

        with allure.step("Performing division calculation of following numbers: {}".format(args)):
            print("\nPerforming division calculation of following numbers: {}".format(args))

            for i, arg in enumerate(args):

                self.enter_digit(arg)

                if i != len(args) - 1:
                    self.app.division.tap()

            print("Formula: {}".format(self.app.screen_formula.formatted_text))
            print("Result: {}".format(self.app.screen_result.formatted_text))

            expected = self.eval_formula(self.app.screen_formula.formatted_text)
            actual = self.app.screen_result.formatted_text
            with allure.step("Perform result (screen) evaluation: "
                             "{} should be equal {}".format(actual, expected)):
                print('Perform result (screen) evaluation: '
                      '{} should be equal {}'.format(actual, expected))
                if '.' in expected:
                    if len(expected[expected.index('.'):]) > 12:
                        assert '%.13f'.format(expected) == '%.13f'.format(actual)
                    else:
                        assert expected == actual

            self.app.equal.tap()
            print("Screen output: {}".format(self.app.screen_result.formatted_text))
