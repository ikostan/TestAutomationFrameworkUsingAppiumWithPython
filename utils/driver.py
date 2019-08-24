from appium import webdriver


class Driver:

	def __init__(self):

		self._desired_capabilities = {
			"platformName": "android",
			"deviceName": "Android Tablet",
			"appPackage": "com.android.calculator2",
			"appActivity": "com.android.calculator2.Calculator"
		}

		self._instance = webdriver.Remote("http://0.0.0.0:4723/wd/hub", self._desired_capabilities)

	@property
	def instance(self):
		"""
		Returns an instance of webdriver.Remote
		:return:
		"""
		return self._instance
