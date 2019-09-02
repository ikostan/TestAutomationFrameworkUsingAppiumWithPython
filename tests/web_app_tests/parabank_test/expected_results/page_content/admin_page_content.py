#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from tests.web_app_tests.parabank_test.expected_results.page_content.base_page_content import BasePageContent


class AdminPageContent(BasePageContent):

	TITLE = BasePageContent.TITLE + 'Administration'

	BASE_URL = 'admin.htm'

	URL = BasePageContent.URL + BASE_URL

	INITIALIZE_BUTTON = 'Initialize'

	CLEAN_BUTTON = 'Clean'
