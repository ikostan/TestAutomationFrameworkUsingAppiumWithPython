"""Calculator Locator Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from appium.webdriver.common.mobileby import MobileBy


class CalculatorPageLocator:
    """
    Contains page locators for Calculator App
    Each locator is a tuple: locator method + locator
    """
    DIGITS = {
        0: (MobileBy.ID, 'com.android.calculator2:id/digit_0'),
        1: (MobileBy.ID, 'com.android.calculator2:id/digit_1'),
        2: (MobileBy.ID, 'com.android.calculator2:id/digit_2'),
        3: (MobileBy.ID, 'com.android.calculator2:id/digit_3'),
        4: (MobileBy.ID, 'com.android.calculator2:id/digit_4'),
        5: (MobileBy.ID, 'com.android.calculator2:id/digit_5'),
        6: (MobileBy.ID, 'com.android.calculator2:id/digit_6'),
        7: (MobileBy.ID, 'com.android.calculator2:id/digit_7'),
        8: (MobileBy.ID, 'com.android.calculator2:id/digit_8'),
        9: (MobileBy.ID, 'com.android.calculator2:id/digit_9'),
    }

    POINT_BTN = (MobileBy.ID, 'com.android.calculator2:id/dec_point')
    PLUS_BTN = (MobileBy.ID, 'com.android.calculator2:id/op_add')
    MINUS_BTN = (MobileBy.ID, 'com.android.calculator2:id/op_sub')
    MULTIPLICATION_BTN = (MobileBy.ID, 'com.android.calculator2:id/op_mul')
    DIVISION_BTN = (MobileBy.ID, 'com.android.calculator2:id/op_div')
    DEL_BTN = (MobileBy.ID, 'com.android.calculator2:id/del')

    CLEAR_BTN = (MobileBy.ID, 'com.android.calculator2:id/clr')
    EQUAL_BTN = (MobileBy.ID, 'com.android.calculator2:id/eq')

    DISPLAY = (MobileBy.ID, 'com.android.calculator2:id/display')
    SCREEN_FORMULA = (MobileBy.ID, 'com.android.calculator2:id/formula')
    SCREEN_RESULT = (MobileBy.ID, 'com.android.calculator2:id/result')

    MORE_OPTIONS = (MobileBy.XPATH, '//android.widget.ImageButton[@content-desc="More options"]')

    OPEN_SOURCE_LICENSE = (MobileBy.ID, 'android:id/title')
