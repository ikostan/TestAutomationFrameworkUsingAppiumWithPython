"""Android Calculator App Basic Buttons Labeling and Visibility Test Case"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
from selenium.common.exceptions import TimeoutException
from tests.android_v7.calculator_tests.calculator_base_testcase import AndroidCalculatorBaseTestCase


@allure.epic('Android Native App')
@allure.parent_suite('Non Functional Test')
@allure.suite("Calculator Test Suite")
@allure.sub_suite("Positive Tests")
@allure.feature("Calculator Basic Buttons")
@allure.story('Buttons Labeling and Visibility')
class TestButtonsLabelingCases(AndroidCalculatorBaseTestCase):
    """
    Android Calculator App Buttons Labeling and Visibility Test Case
    Check all buttons are labeled (0-9, DEL, CLR, . +,-,*,/,=)
    """

    def test_btn_labeling(self):
        """
        All buttons should be labeled appropriately
        :return:
        """
        allure.dynamic.title("Buttons labeling test")
        allure.dynamic.severity(allure.severity_level.CRITICAL)

        # Digits 0-9
        with allure.step("Test 0-9 digits/buttons labeling"):
            for i, btn in enumerate(self.app.digits):
                assert self.app.digits[btn].raw_text == str(i)

        # . button
        with allure.step("Test '.' button labeling"):
            assert self.app.dot.raw_text == '.'

        # +
        with allure.step("Test '+' button labeling"):
            assert self.app.plus.raw_text == '+'

        # -
        with allure.step("Test '-' button labeling"):
            assert self.app.minus.raw_text == '−'

        # *
        with allure.step("Test '*' button labeling"):
            assert self.app.multiplication.raw_text == '×'

        # /
        with allure.step("Test '/' button labeling"):
            assert self.app.division.raw_text == '÷'

        # DEL
        with allure.step("Test 'DEL' button visibility"):
            assert self.app.del_btn.raw_text == 'DEL'

        # CLR button
        with allure.step("Test 'CLR' button labeling"):
            # CLR button is not presented by default
            self.enter_digit(10)
            self.app.equal.tap()
            assert self.app.clr.raw_text == "CLR"
            self.app.clr.tap()

        # =
        with allure.step("Test '=' button labeling"):
            assert self.app.equal.raw_text == '='

    def test_btn_visibility(self):
        """
        Test basic functionality:

        Should be able to open calculator_test app
        Should be able to close the app
        Check if all the numbers are working ( 0 to 9)
        Check for the visibility of all buttons (0-9, DEL, CLR, ., +, -, *, /, =)
        """

        allure.dynamic.title("Buttons visibility test")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        # Digits 0-9
        with allure.step("Test 0-9 digits/buttons visibility"):
            for btn in self.app.buttons:
                assert btn.is_visible

        # . button
        with allure.step("Test '.' button visibility"):
            assert self.app.dot.is_visible

        # +
        with allure.step("Test '+' button visibility"):
            assert self.app.plus.is_visible

        # -
        with allure.step("Test '-' button visibility"):
            assert self.app.minus.is_visible

        # *
        with allure.step("Test '*' button visibility"):
            assert self.app.multiplication.is_visible

        # /
        with allure.step("Test '/' button visibility"):
            assert self.app.division.is_visible

        # DEL
        with allure.step("Test 'DEL' button visibility"):
            assert self.app.del_btn.is_visible

        # CLR button is not presented by default
        with allure.step("Test 'CLR' button visibility"):
            with self.assertRaises(TimeoutException):
                visibility_status = self.app.clr.is_visible

        # =
        with allure.step("Test '=' button visibility"):
            assert self.app.equal.is_visible

        # Display
        with allure.step("Test main display visibility"):
            assert self.app.main_screen.is_visible

