"""
This file is part of the MerchantAPI package.

(c) Miva Inc <https://www.miva.com/>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.

Handles API Request CustomerPriceGroupList_Load_Query. 
Scope: Store.
:see: https://docs.miva.com/json-api/functions/customerpricegrouplist_load_query
"""

import merchantapi.abstract
import merchantapi.model
import merchantapi.response
from merchantapi.request import PriceGroupListLoadQuery
from merchantapi.client import BaseClient as Client
from requests.models import Response as HttpResponse


class CustomerPriceGroupListLoadQuery(PriceGroupListLoadQuery):
	def __init__(self, client: Client = None, customer: merchantapi.model.Customer = None):
		"""
		CustomerPriceGroupListLoadQuery Constructor.

		:param client: Client
		:param customer: Customer
		"""

		super().__init__(client)
		self.customer_id = None
		self.edit_customer = None
		self.customer_login = None
		self.assigned = None
		self.unassigned = None
		if isinstance(customer, merchantapi.model.Customer):
			if customer.get_id():
				self.set_customer_id(customer.get_id())
			elif customer.get_login():
				self.set_edit_customer(customer.get_login())

	def get_function(self):
		"""
		Get the function of the request.

		:returns: str
		"""

		return 'CustomerPriceGroupList_Load_Query'

	def get_customer_id(self) -> int:
		"""
		Get Customer_ID.

		:returns: int
		"""

		return self.customer_id

	def get_edit_customer(self) -> str:
		"""
		Get Edit_Customer.

		:returns: str
		"""

		return self.edit_customer

	def get_customer_login(self) -> str:
		"""
		Get Customer_Login.

		:returns: str
		"""

		return self.customer_login

	def get_assigned(self) -> bool:
		"""
		Get Assigned.

		:returns: bool
		"""

		return self.assigned

	def get_unassigned(self) -> bool:
		"""
		Get Unassigned.

		:returns: bool
		"""

		return self.unassigned

	def set_customer_id(self, customer_id: int) -> 'CustomerPriceGroupListLoadQuery':
		"""
		Set Customer_ID.

		:param customer_id: int
		:returns: CustomerPriceGroupListLoadQuery
		"""

		self.customer_id = customer_id
		return self

	def set_edit_customer(self, edit_customer: str) -> 'CustomerPriceGroupListLoadQuery':
		"""
		Set Edit_Customer.

		:param edit_customer: str
		:returns: CustomerPriceGroupListLoadQuery
		"""

		self.edit_customer = edit_customer
		return self

	def set_customer_login(self, customer_login: str) -> 'CustomerPriceGroupListLoadQuery':
		"""
		Set Customer_Login.

		:param customer_login: str
		:returns: CustomerPriceGroupListLoadQuery
		"""

		self.customer_login = customer_login
		return self

	def set_assigned(self, assigned: bool) -> 'CustomerPriceGroupListLoadQuery':
		"""
		Set Assigned.

		:param assigned: bool
		:returns: CustomerPriceGroupListLoadQuery
		"""

		self.assigned = assigned
		return self

	def set_unassigned(self, unassigned: bool) -> 'CustomerPriceGroupListLoadQuery':
		"""
		Set Unassigned.

		:param unassigned: bool
		:returns: CustomerPriceGroupListLoadQuery
		"""

		self.unassigned = unassigned
		return self

	# noinspection PyTypeChecker
	def send(self) -> 'merchantapi.response.CustomerPriceGroupListLoadQuery':
		return super().send()

	def create_response(self, http_response: HttpResponse, data) -> 'CustomerPriceGroupListLoadQuery':
		"""
		Create a response object from the response data

		:param http_response: requests.models.Response
		:param data:
		:returns: Response
		"""

		return merchantapi.response.CustomerPriceGroupListLoadQuery(self, http_response, data)

	def to_dict(self) -> dict:
		"""
		Reduce the request to a dict

		:override:
		:returns: dict
		"""

		data = super().to_dict()

		if self.customer_id is not None:
			data['Customer_ID'] = self.customer_id
		elif self.edit_customer is not None:
			data['Edit_Customer'] = self.edit_customer
		elif self.customer_login is not None:
			data['Customer_Login'] = self.customer_login

		if self.assigned is not None:
			data['Assigned'] = self.assigned
		if self.unassigned is not None:
			data['Unassigned'] = self.unassigned
		return data
