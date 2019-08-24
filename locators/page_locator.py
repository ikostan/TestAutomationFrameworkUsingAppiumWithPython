from appium.webdriver.common.mobileby import MobileBy


class PageLocator:

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
	EQUAL_BTN = (MobileBy.ID, 'com.android.calculator2:id/eq')

	SCREEN_FORMULA = (MobileBy.ID, 'com.android.calculator2:id/formula')
	SCREEN_RESULT = (MobileBy.ID, 'com.android.calculator2:id/result')
