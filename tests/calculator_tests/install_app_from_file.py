#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import unittest
import allure


@allure.epic('Selendroid Test App')
@allure.parent_suite('Non Functional Test')
@allure.suite("Selendroid App Test Suite")
@allure.sub_suite("Positive Tests")
@allure.feature("App Installation")
@allure.story('App Installation From File')
class TestInstallAppFromFileCase(unittest.TestCase):
	"""
	App source: http://search.maven.org/remotecontent?filepath=io/selendroid/selendroid-test-app/0.17.0/selendroid-test-app-0.17.0.apk
	"""
	pass


if __name__ == '__main__':
	unittest.main()
