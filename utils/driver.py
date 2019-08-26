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

			"automationName": "Appium",
			# "platformVersion": "8.1.0",
			# "browserName": "Chrome",
		}

		self._driver_instance = None

	def set_capability(self, capability_type, capability):
		"""
		Set/add desired capability
		:param capability_type:
		:param capability:
		:return:
		"""
		self._desired_capabilities[capability_type] = capability

	@property
	def capabilities(self):
		"""
		Returns desired capabilities
		:return:
		"""
		return self._desired_capabilities

	@property
	def driver_instance(self):
		"""
		Returns an instance of webdriver.Remote
		:return:
		"""
		if self._driver_instance:
			return self._driver_instance
		else:
			self._driver_instance = webdriver.Remote("http://127.0.0.1:4723/wd/hub",
			                                         self._desired_capabilities)
			return self._driver_instance
