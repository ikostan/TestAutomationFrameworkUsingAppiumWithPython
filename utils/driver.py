#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from appium import webdriver


class Driver:
	"""
	Appium Desired Capabilities: http://appium.io/docs/en/writing-running-appium/caps/
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
		self._instance = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self._desired_capabilities)

	@property
	def capabilities(self):
		return self._desired_capabilities

	@property
	def instance(self):
		"""
		Returns an instance of webdriver.Remote
		:return:
		"""
		return self._instance
