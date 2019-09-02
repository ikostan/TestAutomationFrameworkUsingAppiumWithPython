"""Register Page Content Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from tests.web_app_tests.parabank_test.expected_results.page_content.base_page_content import BasePageContent
from tests.web_app_tests.parabank_test.expected_results.page_content.base_personal_info_content import \
	BasePersonalInfoContent


# TODO: review this one and try to remove BasePersonalInfoContext
class RegisterPageContent(BasePageContent):
	"""
	Register Page Content Class
	Holds fields/data from "Register" form
	"""

	PERSONAL_INFO = BasePersonalInfoContent

	TITLE = BasePageContent.TITLE + 'Register for Free Online Account Access'

	BASE_URL = 'register.htm'

	URL = BasePageContent.URL + BASE_URL

	HEADER = {
		'class': "title",
		'text': 'Signing up is easy!'
	}

	DESCRIPTION = {'text': 'If you have an account with us you can sign-up for free instant online access. '
	                       'You will have to provide some personal information.'}

	REGISTER_FORM = {
		'password': {
			'title': 'Password:',
			'input': {
				'name': "customer.password",
				'class': 'input',
				'type': 'password'
			}
		},
		'confirm': {
			'title': 'Confirm:',
			'input': {
				'name': "repeatedPassword",
				'class': 'input',
				'type': 'password'
			}
		}
	}

	REGISTER_BUTTON = {
		'type': "submit",
		'class': "button",
		'value': "Register"
	}

	WELCOME_MESSAGE = {
		'header': 'Welcome ',
		'message': 'Your account was created successfully. You are now logged in.'
	}
