import unittest
from utils.driver import Driver
from appium.webdriver.common.mobileby import MobileBy


class TestCalculatorCases(unittest.TestCase):

	def setUp(self) -> None:
		self.driver = Driver
	
	def tearDown(self) -> None:
		self.driver.instance.quit()

	def test_calculator_launches(self):
		pass

