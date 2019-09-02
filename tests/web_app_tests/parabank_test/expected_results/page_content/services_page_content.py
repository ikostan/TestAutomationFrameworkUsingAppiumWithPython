"""Services Page Content Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from tests.web_app_tests.parabank_test.expected_results.page_content.base_page_content import BasePageContent


class ServicesPageContent(BasePageContent):
	"""Services Page Content Class"""

	TITLE = BasePageContent.TITLE + 'Services'

	BASE_URL = 'services.htm'

	URL = BasePageContent.URL + BASE_URL
