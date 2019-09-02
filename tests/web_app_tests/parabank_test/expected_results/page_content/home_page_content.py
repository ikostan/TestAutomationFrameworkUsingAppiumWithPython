"""Home Page Content Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from tests.web_app_tests.parabank_test.expected_results.page_content.base_page_content import BasePageContent


class HomePageContent(BasePageContent):
	"""
	Home Page Content Class
	Holds expected context values for home page items
	"""

	BASE_URL = 'index.htm'

	URL = BasePageContent.URL + BASE_URL

	TITLE = BasePageContent.TITLE + 'Welcome | Online Banking'

	ATM_SERVICES = {
		'title': 'ATM Services',
		'Withdraw Funds': {'text': 'Withdraw Funds',
		                   'href': "services/ParaBank"},
		'Transfer Funds': {'text': 'Transfer Funds',
		                   'href': "services/ParaBank"},
		'Check Balances': {'text': 'Check Balances',
		                   'href': "services/ParaBank"},
		'Make Deposits': {'text': 'Make Deposits',
		                  'href': "services/ParaBank"}
	}

	ONLINE_SERVICES = {
		'title': 'Online Services',
		'Bill Pay': {'text': 'Bill Pay',
		             'href': "services/bank?_wadl&_type=xml"},
		'Account History': {'text': 'Account History',
		                    'href': "services/bank?_wadl&_type=xml"},
		'Transfer Funds': {'text': 'Transfer Funds',
		                   'href': "services/bank?_wadl&_type=xml"}
	}

	READ_MORE_SERVICES = {'href': "services.htm",
	                      'text': 'READ MORE'}

	LATEST_NEWS = 'LATEST NEWS'

	READ_MORE_NEWS = {'text': 'READ MORE',
	                  "href": "news.htm"}

