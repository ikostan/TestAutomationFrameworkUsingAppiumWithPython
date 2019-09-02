"""Base Personal Info Page Model Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from tests.web_app_tests.parabank_test.element_object_model.element import Element
from tests.web_app_tests.parabank_test.page_locators.base_personal_info_page_locator import BasePersonalInfoPageLocator


class BasePersonalInfoPageModel:
	"""
	Base Personal Info Page Model Class

    The page object pattern intends creating an object for each web page.
    By following this technique a layer of separation between the test code and technical implementation is created.
    """

	def __init__(self, driver, explicit_wait_time):
		self._driver = driver
		self._explicit_wait_time = explicit_wait_time
		self._locator = BasePersonalInfoPageLocator

	def _create_web_element(self, locator):
		"""Returns base web element"""

		return Element(driver=self._driver,
		               explicit_wait_time=self._explicit_wait_time,
		               locator=locator)

	@property
	def header(self):
		"""
        Returns header text
        :return:
        """
		locator = self._locator.HEADER
		element = self._create_web_element(locator)
		txt = element.text
		return txt

	@property
	def description(self):
		"""
        Returns description text
        :return:
        """
		locator = self._locator.DESCRIPTION
		element = self._create_web_element(locator)
		txt = element.text
		return txt

	@property
	def first_name_title(self):
		"""
        Returns first name title text
        :return:
        """
		locator = self._locator.FIRST_NAME_TITLE
		element = self._create_web_element(locator)
		txt = element.text
		return txt

	def type_first_name(self, first_name: str):
		"""
        Write text into first name input field
        :param first_name:
        :return:
        """
		locator = self._locator.FIRST_NAME_INPUT
		element = self._create_web_element(locator)
		element.write(first_name)
		return None

	@property
	def first_name(self):
		"""
        Returns first name input field value
        :return:
        """
		locator = self._locator.FIRST_NAME_INPUT
		element = self._create_web_element(locator)
		value = element.element_value
		return value

	@property
	def first_name_error(self):
		"""
        Returns first name error.
        Non in case error does not appear.
        :return:
        """
		locator = self._locator.FIRST_NAME_ERROR
		element = self._create_web_element(locator)
		txt = element.text
		return txt

	@property
	def last_name_title(self):
		"""
        Returns last name title text
        :return:
        """
		locator = self._locator.LAST_NAME_TITLE
		element = self._create_web_element(locator)
		txt = element.text
		return txt

	def type_last_name(self, last_name: str):
		"""
        Write text into last name input field
        :param last_name:
        :return:
        """
		locator = self._locator.LAST_NAME_INPUT
		element = self._create_web_element(locator)
		element.write(last_name)
		return None

	@property
	def last_name(self):
		"""
        Returns last name input field value
        :return:
        """
		locator = self._locator.LAST_NAME_INPUT
		element = self._create_web_element(locator)
		value = element.element_value
		return value

	@property
	def last_name_error(self):
		"""
        Returns last name error.
        :return:
        """
		locator = self._locator.LAST_NAME_ERROR
		element = self._create_web_element(locator)
		txt = element.text
		return txt

	@property
	def address_title(self):
		"""
        Returns address title text
        :return:
        """
		locator = self._locator.ADDRESS_TITLE
		element = self._create_web_element(locator)
		txt = element.text
		return txt

	def type_address(self, address: str):
		"""
        Write text into address input field
        :param address:
        :return:
        """
		locator = self._locator.ADDRESS_INPUT
		element = self._create_web_element(locator)
		element.write(address)
		return None

	@property
	def address(self):
		"""
        Returns address input field value
        :return:
        """
		locator = self._locator.ADDRESS_INPUT
		element = self._create_web_element(locator)
		value = element.element_value
		return value

	@property
	def address_error(self):
		"""
        Returns address name error.
        :return:
        """
		locator = self._locator.ADDRESS_ERROR
		element = self._create_web_element(locator)
		txt = element.text
		return txt

	@property
	def city_title(self):
		"""
        Returns address title text
        :return:
        """
		locator = self._locator.CITY_TITLE
		element = self._create_web_element(locator)
		txt = element.text
		return txt

	def type_city(self, city: str):
		"""
        Write text into city input field
        :param city:
        :return:
        """
		locator = self._locator.CITY_INPUT
		element = self._create_web_element(locator)
		element.write(city)
		return None

	@property
	def city(self):
		"""
        Returns city input field value
        :return:
        """
		locator = self._locator.CITY_INPUT
		element = self._create_web_element(locator)
		value = element.element_value
		return value

	@property
	def city_error(self):
		"""
        Returns city name error.
        :return:
        """
		locator = self._locator.CITY_ERROR
		element = self._create_web_element(locator)
		txt = element.text
		return txt

	@property
	def state_title(self):
		"""
        Returns state title text
        :return:
        """
		locator = self._locator.STATE_TITLE
		element = self._create_web_element(locator)
		txt = element.text
		return txt

	def type_state(self, state: str):
		"""
        Write text into state input field
        :param state:
        :return:
        """
		locator = self._locator.STATE_INPUT
		element = self._create_web_element(locator)
		element.write(state)
		return None

	@property
	def state(self):
		"""
        Returns state input field value
        :return:
        """
		locator = self._locator.STATE_INPUT
		element = self._create_web_element(locator)
		value = element.element_value
		return value

	@property
	def state_error(self):
		"""
        Returns state name error.
        :return:
        """
		locator = self._locator.STATE_ERROR
		element = self._create_web_element(locator)
		txt = element.text
		return txt

	@property
	def zip_code_title(self):
		"""
        Returns zip code title text
        :return:
        """
		locator = self._locator.ZIP_CODE_TITLE
		element = self._create_web_element(locator)
		txt = element.text
		return txt

	def type_zip_code(self, zip_code: str):
		"""
        Write text into zip_code input field
        :param zip_code:
        :return:
        """
		locator = self._locator.ZIP_CODE_INPUT
		element = self._create_web_element(locator)
		element.write(zip_code)
		return None

	@property
	def zip_code(self):
		"""
        Returns zip code input field value
        :return:
        """
		locator = self._locator.ZIP_CODE_INPUT
		element = self._create_web_element(locator)
		value = element.element_value
		return value

	@property
	def zip_code_error(self):
		"""
        Returns zip code error.
        :return:
        """
		locator = self._locator.ZIP_CODE_ERROR
		element = self._create_web_element(locator)
		txt = element.text
		return txt

	@property
	def phone_title(self):
		"""
        Returns phone title text
        :return:
        """
		locator = self._locator.PHONE_TITLE
		element = self._create_web_element(locator)
		txt = element.text
		return txt

	def type_phone(self, phone_number: str):
		"""
        Write text into phone input field
        :param phone_number:
        :return:
        """
		locator = self._locator.PHONE_INPUT
		element = self._create_web_element(locator)
		element.write(phone_number)
		return None

	@property
	def phone(self):
		"""
        Returns phone input field value
        :return:
        """
		locator = self._locator.PHONE_INPUT
		element = self._create_web_element(locator)
		value = element.element_value
		return value

	@property
	def ssn_title(self):
		"""
        Returns SSN title text
        :return:
        """
		locator = self._locator.SSN_TITLE
		element = self._create_web_element(locator)
		txt = element.text
		return txt

	def type_ssn(self, ssn: str):
		"""
        Write text into ssn input field
        :param ssn:
        :return:
        """
		locator = self._locator.SSN_INPUT
		element = self._create_web_element(locator)
		element.write(ssn)
		return None

	@property
	def ssn(self):
		"""
        Returns SSN input field value
        :return:
        """
		locator = self._locator.SSN_INPUT
		element = self._create_web_element(locator)
		value = element.element_value
		return value

	@property
	def ssn_error(self):
		"""
        Returns SSN error.
        :return:
        """
		locator = self._locator.SSN_ERROR
		element = self._create_web_element(locator)
		txt = element.text
		return txt
