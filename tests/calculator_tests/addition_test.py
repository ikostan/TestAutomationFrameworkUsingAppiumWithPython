"""Calculator App Test Case: Addition"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import unittest


class TestAdditionCase(unittest.TestCase):

	"""
	This suite tests the current code in the calculator_test.
	Any tests that fail will be in red text with a red x and tests that pass will have a green check mark.
	You can click on the text for any case to see what test code is being run.
	The code can be read in rough English to understand what is being tested.

	Terminology
	Addend + Addend = Sum
	Minuend - Subtrahend = Difference
	Multiplicand * Multiplier = Product
	Dividend / Divisor = quotient
	calculator_test Test Suite

	Should be able to add two positive integers numbers ‣
	Should be able to add a negative integer to a positive floating point number ‣
	Should be able to add a floating point number to an integer ‣
	Should be able to add an integer to a floating point number ‣
	Should be able to add two floating point numbers ‣
	Should be able to add a negative integer and zero ‣
	Should be able to add zero and a positive integer ‣
	Should be able to add a negative integer with a positive number ‣
	Should be able to add two large positive integers ‣
	Should be able to add a negative floating point and a positive integer ‣
	Should be able to add a positive integer to the results of a previous operation ‣
	Should be able to add a positive floating point number to the results of a previous operation ‣
	Should be able to add a floating point number with many decimal places to a previous result ‣
	Should be able to add a large integer to a previous result

	Source: https://mozilla.github.io/calculator/test/?grep=Unit%20Tests%20Addition
	"""

	def setUp(self) -> None:
		self.driver = Driver()
		self.driver.driver_instance.implicitly_wait(3)

	def tearDown(self) -> None:
		if self.driver.driver_instance:
			self.driver.driver_instance.quit()
			self.driver = None

	def test_something(self):
		pass
