"""Login Page Content Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from tests.web_app_tests.parabank_test.expected_results.page_content.base_page_content import BasePageContent


class LoginPageContent(BasePageContent):
	"""Login Page Content Class"""

	TITLE_ERROR = BasePageContent.TITLE + 'Error'

	URL = BasePageContent.URL + 'login.htm'

	ERROR_TITLE = 'Error!'
	NO_SUCH_USER_ERROR_MESSAGE = 'The username and password could not be verified.'
	EMPTY_FIELDS_ERROR_MESSAGE = 'Please enter a username and password.'

