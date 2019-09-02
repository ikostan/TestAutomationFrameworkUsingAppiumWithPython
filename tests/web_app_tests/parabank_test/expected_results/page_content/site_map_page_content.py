"""Site Map Page Content Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from tests.web_app_tests.parabank_test.expected_results.page_content.base_page_content import BasePageContent


class SiteMapPageContent(BasePageContent):
	"""
	Site Map Page Content Class
	Holds expected context values for About web page items
	"""

	TITLE = BasePageContent.TITLE + 'Site Map'

	BASE_URL = 'sitemap.htm'

	URL = BasePageContent.URL + BASE_URL
