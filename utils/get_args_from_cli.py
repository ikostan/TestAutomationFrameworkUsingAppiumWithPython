"""Extract arguments from CLI"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import sys


def get_args():
    """
    Reads arguments from CLI and returns them as dictionary.
    Helps running Python unittest with command-line arguments.
    Raises Exception if one of the required arguments is missing.
    :return:
    """

    is_headless, browser_name, env, platform_name, device_name, automation_name, \
    platform_version, app, app_activity, app_package = \
        None, None, None, None, None, None, None, None, None, None

    for param in sys.argv:

        # Test environment (mainly for web testing)
        if '--env=' in param:
            env = str(param).replace('--env=', '')
            print("\n--env={}".format(env))

        # Selenium
        if '--is_headless=' in param:
            is_headless = True if str(param).replace('--is_headless=', '') == 'True' else False
            print("\n--is_headless={}".format(is_headless))

        # Appium Desired Capabilities
        # http://appium.io/docs/en/writing-running-appium/caps/

        # Name of mobile web browser to automate. Should be an empty string if automating an app instead.
        # 'Safari' for iOS and 'Chrome', 'Chromium', or 'Browser' for Android
        if '--browserName=' in param:
            browser_name = str(param).replace('--browserName=', '')
            print("\n--browserName={}".format(browser_name))

        # Which mobile OS platform to use
        # iOS, Android, or FirefoxOS
        if "--platformName=" in param:
            platform_name = str(param).replace('--platformName=', '')
            print("\n--platformName={}".format(platform_name))

        # The kind of mobile device or emulator to use
        if "--deviceName=" in param:
            device_name = str(param).replace('--deviceName=', '')
            print("\n--deviceName={}".format(device_name))

        # Which automation engine to use
        # Appium (default) or Selendroid or UiAutomator2 or Espresso for Android
        # or XCUITest for iOS or YouiEngine for application built with You.i Engine
        if "--automationName=" in param:
            automation_name = str(param).replace('--automationName=', '')
            print("\n--automationName={}".format(automation_name))

        # Mobile OS version
        # e.g., 7.1, 4.4
        if "--platformVersion=" in param:
            platform_version = str(param).replace('--platformVersion=', '')
            print("\n--platformVersion={}".format(platform_version))

        # The absolute local path or remote http URL to a .ipa file (IOS),
        # .app folder (IOS Simulator), .apk file (Android) or .apks file (Android App Bundle),
        # or a .zip file containing one of these (for .app, the .app folder must be the root of the zip file).
        if "--app=" in param:
            app = str(param).replace('--app=', '')
            print("\n--platformVersion={}".format(app))

        # Android Only
        # Activity name for the Android activity you want to launch from your package.
        # e.g. com.example.android.myApp
        if "--appActivity=" in param:
            app_activity = str(param).replace('--appActivity=', '')
            print("\n--appActivity={}".format(app_activity))

        # Java package of the Android app you want to run.
        if "--appPackage=" in param:
            app_package = str(param).replace('--appPackage=', '')
            print("\n--appPackage={}".format(app_package))

    '''
    if env is None:
        raise Exception("Please add '--env=<data>' argument to the command line")

    if browser is None:
        raise Exception("Please add '--browser=<data>' argument to the command line")

    if is_headless is None:
        raise Exception("Please add '--is_headless=<data>' argument to the command line")
    
    if platform_name is None:
        raise Exception("Please add '--platformName=<data>' argument to the command line")

    if device_name is None:
        raise Exception("Please add '--deviceName=<data>' argument to the command line")

    if automation_name is None:
        raise Exception("Please add '--automationName=<data>' argument to the command line")
    '''

    return {'env': env,
            'browserName': browser_name,
            'is_headless': is_headless,
            'platformName': platform_name,
            'deviceName': device_name,
            'automationName': automation_name,
            'platformVersion': platform_version,
            'app': app,
            'appActivity': app_activity,
            'appPackage': app_package}
