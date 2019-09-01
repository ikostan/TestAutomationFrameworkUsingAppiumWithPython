"""Bank Account Content Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from tests.web_app_tests.parabank_test.expected_results.page_content.base_page_content import BasePageContent


class BankAccountContent(BasePageContent):
	"""
	Bank Account Content Class

	Holds expected results for Bank Account web page
	"""

	ACCOUNT_SERVICES_MENU = {
		'welcome_message': "Welcome ",
		'title': 'Account Services',
		"menu_items": {
			'open_new_account': {'text': 'Open New Account',
			                     "href": "/parabank/openaccount.htm"},
			'account_overview': {'text': 'Accounts Overview',
			                     "href": "/parabank/overview.htm"},
			'transfer_funds': {'text': 'Transfer Funds',
			                   "href": "/parabank/transfer.htm"},
			'bill_pay': {'text': 'Bill Pay',
			             "href": "/parabank/billpay.htm"},
			'find_transactions': {'text': 'Find Transactions',
			                      "href": "/parabank/findtrans.htm"},
			'update_info': {'text': 'Update Contact Info',
			                "href": "/parabank/updateprofile.htm"},
			'request_loan': {'text': 'Request Loan',
			                 "href": "/parabank/requestloan.htm"},
			'log_out': {'text': 'Log Out',
			            "href": "/parabank/logout.htm"}
		}
	}

