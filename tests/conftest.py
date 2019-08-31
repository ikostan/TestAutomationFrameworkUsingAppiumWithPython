"""Pass different values to a test function, depending on command line options"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from pytest import fixture


def pytest_addoption(parser):
	"""
	Pass different values to a test function, depending on command line options
	Source: https://docs.pytest.org/en/latest/example/simple.html
	:param parser:
	:return:
	"""

	parser.addoption('--env',
	                 action="store",
	                 help="Base URL/Environment")

	parser.addoption('--browserName',
	                 action="store",
	                 help="Name of mobile web browser to automate. "
	                      "Should be an empty string if automating an app instead."
	                      "Samples: 'Safari' for iOS and 'Chrome', 'Chromium', or 'Browser' for Android")

	parser.addoption('--is_headless',
	                 action="store",
	                 help="Headless browser run without a UI")

	parser.addoption('--automationName',
	                 action="store",
	                 help="Which automation engine to use."
	                      "\nAppium (default) or Selendroid or UiAutomator2 or Espresso for Android or "
	                      "XCUITest for iOS or YouiEngine for application built with You.i Engine")

	parser.addoption('--platformName',
	                 action="store",
	                 help="Which mobile OS platform to use: iOS, Android, or FirefoxOS")

	parser.addoption('--platformVersion',
	                 action="store",
	                 help="Mobile OS version e.g., 7.1, 4.4")

	parser.addoption('--deviceName',
	                 action="store",
	                 help="The kind of mobile device or emulator to use: iPhone Simulator, Android Emulator...")

	parser.addoption('--app',
	                 action="store",
	                 help="The absolute local path or remote http URL to a .ipa file (IOS), "
	                      ".app folder (IOS Simulator), .apk file (Android) or "
	                      ".apks file (Android App Bundle), or a .zip file containing one of these "
	                      "(for .app, the .app folder must be the root of the zip file).")

	parser.addoption('--appActivity',
	                 action="store",
	                 help="Activity name for the Android activity you want to launch from your package. "
	                      "This often needs to be preceded by a . (e.g., .MainActivity instead of MainActivity).")

	parser.addoption('--appPackage',
	                 action="store",
	                 help="Java package of the Android app you want to run. "
	                      "By default this capability is received from the package manifest (@package attribute value)")


@fixture(scope='session')
def env(request):
	return request.config.getoption("--env")


@fixture(scope='session')
def browser(request):
	return request.config.getoption("--browserName")


@fixture(scope='session')
def is_headless(request):
	return request.config.getoption("--is_headless")


@fixture(scope='session')
def automation_name(request):
	return request.config.getoption("--automationName")


@fixture(scope='session')
def platform_name(request):
	return request.config.getoption("--platformName")


@fixture(scope='session')
def platform_version(request):
	return request.config.getoption("--platformVersion")


@fixture(scope='session')
def device_name(request):
	return request.config.getoption("--deviceName")


@fixture(scope='session')
def app(request):
	return request.config.getoption("--app")


@fixture(scope='session')
def app_activity(request):
	return request.config.getoption("--appActivity")


@fixture(scope='session')
def app_package(request):
	return request.config.getoption("--appPackage")

