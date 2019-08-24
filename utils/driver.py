from appium import webdriver


class Driver:

	def __init__(self):
		desired_capabilities = {
			"platformName": "android",
			"deviceName": "Android Tablet",
			"appPackage": "com.android.calculator2",
			"appActivity": "com.android.calculator2.Calculator"
		}

		self.instance = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_capabilities)
