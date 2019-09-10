"""Android App Test: apk package installation"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import unittest
import allure
import pytest


@allure.epic('Selendroid Test App')
@allure.parent_suite('Non Functional Test')
@allure.suite("Selendroid App Test Suite")
@allure.sub_suite("Positive Tests")
@allure.feature("App Installation")
@allure.story('App Installation From File')
class TestInstallAppFromFileCase(unittest.TestCase):
	"""
	Android App Test: apk package installation
	App source: http://search.maven.org/remotecontent?filepath=io/selendroid/selendroid-test-app/0.17.0/selendroid-test-app-0.17.0.apk
	"""

	@pytest.mark.skip("Not implemented")
	def test_app_installation_from_file(self):
		pass

