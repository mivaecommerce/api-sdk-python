"""
This file is part of the MerchantAPI package.

(c) Miva Inc <https://www.miva.com/>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.

Handles API Request AvailabilityGroupPaymentMethod_Update_Assigned. 
Scope: Store.
:see: https://docs.miva.com/json-api/functions/availabilitygrouppaymentmethod_update_assigned
"""

import merchantapi.abstract
import merchantapi.model
import merchantapi.response
from merchantapi.client import BaseClient as Client
from requests.models import Response as HttpResponse


class AvailabilityGroupPaymentMethodUpdateAssigned(merchantapi.abstract.Request):
	def __init__(self, client: Client = None, availability_group: merchantapi.model.AvailabilityGroup = None):
		"""
		AvailabilityGroupPaymentMethodUpdateAssigned Constructor.

		:param client: Client
		:param availability_group: AvailabilityGroup
		"""

		super().__init__(client)
		self.availability_group_id = None
		self.edit_availability_group = None
		self.availability_group_name = None
		self.module_code = None
		self.method_code = None
		self.payment_card_type_id = None
		self.assigned = None
		if isinstance(availability_group, merchantapi.model.AvailabilityGroup):
			if availability_group.get_id():
				self.set_availability_group_id(availability_group.get_id())
			elif availability_group.get_name():
				self.set_edit_availability_group(availability_group.get_name())

	def get_function(self):
		"""
		Get the function of the request.

		:returns: str
		"""

		return 'AvailabilityGroupPaymentMethod_Update_Assigned'

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

	def get_module_code(self) -> str:
		"""
		Get Module_Code.

		:returns: str
		"""

		return self.module_code

	def get_method_code(self) -> str:
		"""
		Get Method_Code.

		:returns: str
		"""

		return self.method_code

	def get_payment_card_type_id(self) -> int:
		"""
		Get PaymentCardType_ID.

		:returns: int
		"""

		return self.payment_card_type_id

	def get_assigned(self) -> bool:
		"""
		Get Assigned.

		:returns: bool
		"""

		return self.assigned

	def set_availability_group_id(self, availability_group_id: int) -> 'AvailabilityGroupPaymentMethodUpdateAssigned':
		"""
		Set AvailabilityGroup_ID.

		:param availability_group_id: int
		:returns: AvailabilityGroupPaymentMethodUpdateAssigned
		"""

		self.availability_group_id = availability_group_id
		return self

	def set_edit_availability_group(self, edit_availability_group: str) -> 'AvailabilityGroupPaymentMethodUpdateAssigned':
		"""
		Set Edit_AvailabilityGroup.

		:param edit_availability_group: str
		:returns: AvailabilityGroupPaymentMethodUpdateAssigned
		"""

		self.edit_availability_group = edit_availability_group
		return self

	def set_availability_group_name(self, availability_group_name: str) -> 'AvailabilityGroupPaymentMethodUpdateAssigned':
		"""
		Set AvailabilityGroup_Name.

		:param availability_group_name: str
		:returns: AvailabilityGroupPaymentMethodUpdateAssigned
		"""

		self.availability_group_name = availability_group_name
		return self

	def set_module_code(self, module_code: str) -> 'AvailabilityGroupPaymentMethodUpdateAssigned':
		"""
		Set Module_Code.

		:param module_code: str
		:returns: AvailabilityGroupPaymentMethodUpdateAssigned
		"""

		self.module_code = module_code
		return self

	def set_method_code(self, method_code: str) -> 'AvailabilityGroupPaymentMethodUpdateAssigned':
		"""
		Set Method_Code.

		:param method_code: str
		:returns: AvailabilityGroupPaymentMethodUpdateAssigned
		"""

		self.method_code = method_code
		return self

	def set_payment_card_type_id(self, payment_card_type_id: int) -> 'AvailabilityGroupPaymentMethodUpdateAssigned':
		"""
		Set PaymentCardType_ID.

		:param payment_card_type_id: int
		:returns: AvailabilityGroupPaymentMethodUpdateAssigned
		"""

		self.payment_card_type_id = payment_card_type_id
		return self

	def set_assigned(self, assigned: bool) -> 'AvailabilityGroupPaymentMethodUpdateAssigned':
		"""
		Set Assigned.

		:param assigned: bool
		:returns: AvailabilityGroupPaymentMethodUpdateAssigned
		"""

		self.assigned = assigned
		return self

	# noinspection PyTypeChecker
	def send(self) -> 'merchantapi.response.AvailabilityGroupPaymentMethodUpdateAssigned':
		return super().send()

	def create_response(self, http_response: HttpResponse, data) -> 'AvailabilityGroupPaymentMethodUpdateAssigned':
		"""
		Create a response object from the response data

		:param http_response: requests.models.Response
		:param data:
		:returns: Response
		"""

		return merchantapi.response.AvailabilityGroupPaymentMethodUpdateAssigned(self, http_response, data)

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

		data['Module_Code'] = self.module_code
		data['Method_Code'] = self.method_code
		if self.payment_card_type_id is not None:
			data['PaymentCardType_ID'] = self.payment_card_type_id
		data['Assigned'] = self.assigned
		return data
