"""
This file is part of the MerchantAPI package.

(c) Miva Inc <https://www.miva.com/>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.

Handles API Request AvailabilityGroupProductList_Load_Query. 
Scope: Store.
:see: https://docs.miva.com/json-api/functions/availabilitygroupproductlist_load_query
"""

import merchantapi.abstract
import merchantapi.model
import merchantapi.response
from merchantapi.request import ProductListLoadQuery
from merchantapi.client import BaseClient as Client
from requests.models import Response as HttpResponse


class AvailabilityGroupProductListLoadQuery(ProductListLoadQuery):
	def __init__(self, client: Client = None, availability_group: merchantapi.model.AvailabilityGroup = None):
		"""
		AvailabilityGroupProductListLoadQuery Constructor.

		:param client: Client
		:param availability_group: AvailabilityGroup
		"""

		super().__init__(client)
		self.availability_group_id = None
		self.edit_availability_group = None
		self.availability_group_name = None
		self.assigned = None
		self.unassigned = None
		if isinstance(availability_group, merchantapi.model.AvailabilityGroup):
			if availability_group.get_id():
				self.set_availability_group_id(availability_group.get_id())

	def get_function(self):
		"""
		Get the function of the request.

		:returns: str
		"""

		return 'AvailabilityGroupProductList_Load_Query'

	def get_availability_group_id(self) -> int:
		"""
		Get AvailabilityGroup_ID.

		:returns: int
		"""

		return self.availability_group_id

	def get_edit_availability_group(self) -> str:
		"""
		Get Edit_AvailabilityGroup.

		:returns: str
		"""

		return self.edit_availability_group

	def get_availability_group_name(self) -> str:
		"""
		Get AvailabilityGroup_Name.

		:returns: str
		"""

		return self.availability_group_name

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

	def set_availability_group_id(self, availability_group_id: int) -> 'AvailabilityGroupProductListLoadQuery':
		"""
		Set AvailabilityGroup_ID.

		:param availability_group_id: int
		:returns: AvailabilityGroupProductListLoadQuery
		"""

		self.availability_group_id = availability_group_id
		return self

	def set_edit_availability_group(self, edit_availability_group: str) -> 'AvailabilityGroupProductListLoadQuery':
		"""
		Set Edit_AvailabilityGroup.

		:param edit_availability_group: str
		:returns: AvailabilityGroupProductListLoadQuery
		"""

		self.edit_availability_group = edit_availability_group
		return self

	def set_availability_group_name(self, availability_group_name: str) -> 'AvailabilityGroupProductListLoadQuery':
		"""
		Set AvailabilityGroup_Name.

		:param availability_group_name: str
		:returns: AvailabilityGroupProductListLoadQuery
		"""

		self.availability_group_name = availability_group_name
		return self

	def set_assigned(self, assigned: bool) -> 'AvailabilityGroupProductListLoadQuery':
		"""
		Set Assigned.

		:param assigned: bool
		:returns: AvailabilityGroupProductListLoadQuery
		"""

		self.assigned = assigned
		return self

	def set_unassigned(self, unassigned: bool) -> 'AvailabilityGroupProductListLoadQuery':
		"""
		Set Unassigned.

		:param unassigned: bool
		:returns: AvailabilityGroupProductListLoadQuery
		"""

		self.unassigned = unassigned
		return self

	# noinspection PyTypeChecker
	def send(self) -> 'merchantapi.response.AvailabilityGroupProductListLoadQuery':
		return super().send()

	def create_response(self, http_response: HttpResponse, data) -> 'AvailabilityGroupProductListLoadQuery':
		"""
		Create a response object from the response data

		:param http_response: requests.models.Response
		:param data:
		:returns: Response
		"""

		return merchantapi.response.AvailabilityGroupProductListLoadQuery(self, http_response, data)

	def to_dict(self) -> dict:
		"""
		Reduce the request to a dict

		:override:
		:returns: dict
		"""

		data = super().to_dict()

		if self.availability_group_id is not None:
			data['AvailabilityGroup_ID'] = self.availability_group_id
		elif self.edit_availability_group is not None:
			data['Edit_AvailabilityGroup'] = self.edit_availability_group
		elif self.availability_group_name is not None:
			data['AvailabilityGroup_Name'] = self.availability_group_name

		if self.assigned is not None:
			data['Assigned'] = self.assigned
		if self.unassigned is not None:
			data['Unassigned'] = self.unassigned
		return data
