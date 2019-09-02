"""Accounts Overview Page Content Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from tests.web_app_tests.parabank_test.expected_results.page_content.base_page_content import BasePageContent


class AccountsOverviewPageContent(BasePageContent):
	"""Accounts Overview Page Content Class"""

	TITLE = BasePageContent.TITLE + 'Accounts Overview'

	URL = BasePageContent.URL + 'overview.htm'

