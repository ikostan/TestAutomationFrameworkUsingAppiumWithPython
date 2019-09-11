"""Calculator > License View Locator Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class LicensePageLocator:
    """
    Contains page locators for calculators app > license view
    Each locator is a tuple: locator method + locator
    """

    HEADER = (By.XPATH, '/html/body/h3')
    CRC = (By.XPATH, '/html/body/ul/li')
    FULL_TEXT = (By.XPATH, '/html/body/pre')
    ARROW_BTN = (MobileBy.ACCESSIBILITY_ID, 'Navigate up')
