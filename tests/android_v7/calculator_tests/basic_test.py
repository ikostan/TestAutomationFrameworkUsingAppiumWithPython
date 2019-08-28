"""Android Calculator App Basic Functionality Test Case"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import pytest
from selenium.common.exceptions import TimeoutException
from tests.android_v7_calculator_tests.calculator_base_testcase import AndroidCalculatorBaseTestCase


@allure.epic('Android Native App')
@allure.parent_suite('Functional Test')
@allure.suite("Calculator Test Suite")
@allure.sub_suite("Positive Tests")
@allure.feature("Calculator Basic Buttons")
@allure.story('Basic Functionality')
class TestBasicCalculatorCases(AndroidCalculatorBaseTestCase):
    """
    Android Calculator App Basic Functionality Test Case

    Test basic functionality:

    Should be able to open calculator_test app
    Should be able to enter digits
    Should be able to use "=" button
    Should be able to use "DEL" button
    Should be able to use "CLR" button
    Should be able to see input/output
    Should be able to close the app
    Check for the visibility of all buttons (0-9, DEL, CLR, . +,-,*,/,=)
    """

    @pytest.mark.skip("Not implemented")
    def test_btn_labeling(self):
        """
        All buttons should be labeled appropriately
        :return:
        """
        allure.dynamic.title("Buttons labeling test")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step(""):
            pass

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

    def test_entering_digits(self):
        """
        Should be able to open calculator_test app
        Should be able to enter digits
        Should be able to see input/output
        Should be able to close the app
        :return:
        """

        allure.dynamic.title("0-9 buttons basic functionality test")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Enter digits 0-9"):
            self.enter_number("0123456789")

        with allure.step("Verify screen output"):
            assert self.app.screen_formula.label == '0123456789'

    def test_equal_btn(self):
        """
        Should be able to open calculator_test app
        Should be able to enter digits
        Should be able to use "=" button
        Should be able to see input/output
        Should be able to close the app
        :return:
        """

        allure.dynamic.title("'=' basic functionality test")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Enter digits 0-9"):
            self.enter_number("0123456789")

        with allure.step("Press '=' button"):
            self.app.equal.tap()

        with allure.step("Verify screen output"):
            assert self.app.screen_result.label == '123456789'

    def test_clear_btn(self):
        """
        Should be able to open calculator_test app
        Should be able to use "CLR" button
        Should be able to close the app
        :return:
        """

        allure.dynamic.title("'CLR' basic functionality test")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Enter digits 0-9"):
            self.enter_number("0123456789")

        with allure.step("Press '=' button"):
            self.app.equal.tap()

        with allure.step("Test 'CLR' button visibility"):
            assert self.app.clr.is_visible

        with allure.step("Press 'CLR' button"):
            self.app.clr.tap()

        with allure.step("Verify formula screen output"):
            assert self.app.screen_formula.label == ''

        with allure.step("Verify result screen output"):
            assert self.app.screen_result.label == ''

    def test_delete_btn(self):
        """
        Should be able to open calculator_test app
        Should be able to enter digits
        Should be able to use "DEL" button
        Should be able to see input/output
        Should be able to close the app
        :return:
        """

        allure.dynamic.title("'DEL' basic functionality test")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Enter digits 0-9"):
            self.enter_number("0123456789")

        with allure.step("Test 'DEL' button"):

            for index in range(len('0123456789')):
                with allure.step("Press 'DEL' button"):
                    self.app.del_btn.tap()

                with allure.step("Verify formula screen output"):
                    assert self.app.screen_formula.label == '0123456789'[0:len('0123456789') - (1 + index)]

        with allure.step("Verify formula screen output"):
            assert self.app.screen_formula.label == ''

        with allure.step("Verify result screen output"):
            assert self.app.screen_result.label == ''
