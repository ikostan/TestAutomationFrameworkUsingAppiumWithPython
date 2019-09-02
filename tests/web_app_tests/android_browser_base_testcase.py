"""Base Web App Test Case Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import os
import unittest
import allure

from allure_commons.types import AttachmentType

from utils.driver import Driver
from utils.get_args_from_cli import get_args


class AndroidBrowserBaseTestCase(unittest.TestCase):
    """
    Base Web App Test Case Class
    Take care of basic test setup
    """

    @classmethod
    def setUpClass(cls) -> None:

        with allure.step("Start Appium Service"):
            # How to programmatically start/stop an Appium server.
            # Source: https://stackoverflow.com/questions/51734382/how-to-start-appium-server-programmatically-in-python
            # Source: https://github.com/appium/python-client/blob/master/appium/webdriver/appium_service.py
            # Source: https://discuss.appium.io/t/launching-and-stopping-appium-server-programmtically/700/2
            os.system("start /B start cmd.exe @cmd /k appium --relaxed-security")

        with allure.step("Set Driver to None"):
            cls.driver = None

        with allure.step("Get args from CLI"):
            cls.args = get_args()

    @classmethod
    def tearDownClass(cls) -> None:
        with allure.step("Close Page Model > Set driver to None"):
            if cls.driver:
                if cls.driver.driver_instance:
                    cls.driver.driver_instance.quit()
                cls.driver = None

        with allure.step("Stop Appium Service"):
            # Stop Appium Service
            # Source: https://discuss.appium.io/t/launching-and-stopping-appium-server-programmtically/700/2
            os.system('taskkill /F /IM node.exe')

    def setUp(self) -> None:

        with allure.step("Instantiate Driver"):
            self.driver = Driver()

        with allure.step("Set desired capabilities"):
            self.driver.set_capability("platformName",
                                       self.args["platformName"])

            self.driver.set_capability("deviceName",
                                       self.args["deviceName"])

            self.driver.set_capability("automationName",
                                       self.args["automationName"])

            self.driver.set_capability("browserName",
                                       "Chrome")

            self.driver.set_capability('chromedriverExecutable',
                                       'C:\\Users\\superadmin\\Documents\\GitHub\\'
                                       'TEST_AUTOMATION_FRAMEWORK_USING_APPIUM_WITH_PYTHON\\'
                                       'drivers\\chromedriver\\v2_44\\chromedriver.exe')

        # NOTE: In addCleanup, the first in, is executed last.
        with allure.step("Add clean up methods"):
            self.addCleanup(self.driver.driver_instance.quit)
            self.addCleanup(self.snap_shot)

        with allure.step("Get driver/page instance"):
            self.driver.driver_instance.implicitly_wait(3)
            self.driver = self.driver.driver_instance

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
                self.driver.get_screenshot_as_file(file_name)
                allure.attach.file('./' + file_name, attachment_type=AttachmentType.PNG)
                os.remove(file_name)

                # Get Appium Server Logs:
                # Source: https://appium.readthedocs.io/en/stable/en/commands/session/logs/get-log/#get-logs
                appium_server_log = self.driver.get_log('server')
                file_name = "./appium_server_log.txt"
                with open(file_name, "w") as f:
                    for dictionary in appium_server_log:
                        for k in dictionary:
                            f.write("{} : {}\n".format(k, dictionary[k]))
                        f.write("\n")

                allure.attach.file(file_name, attachment_type=AttachmentType.TEXT)
                os.remove(file_name)
