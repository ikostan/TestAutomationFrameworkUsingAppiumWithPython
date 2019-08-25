#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from appium import webdriver


class Driver:
	"""
	Sources:
	Appium Desired Capabilities: http://appium.io/docs/en/writing-running-appium/caps/
	Python appium.webdriver.Remote() Examples: https://www.programcreek.com/python/example/100038/appium.webdriver.Remote
	Create New Session: https://appium.readthedocs.io/en/stable/en/commands/session/create/
	"""

	def __init__(self):
		self._desired_capabilities = {
			"platformName": "android",
			"deviceName": "Android Tablet",
			"appPackage": "com.android.calculator2",
			"appActivity": "com.android.calculator2.calculator_test",
			"automationName": "Appium",
			"platformVersion": "7.0",
		}

		print("Opening test app: {}...".format(self._desired_capabilities["appActivity"]))
		self._driver_instance = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self._desired_capabilities)

	@property
	def capabilities(self):
		return self._desired_capabilities

	@property
	def driver_instance(self):
		"""
		Returns an instance of webdriver.Remote
		:return:
		"""
		return self._driver_instance
