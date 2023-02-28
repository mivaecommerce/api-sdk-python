"""
This file is part of the MerchantAPI package.

(c) Miva Inc <https://www.miva.com/>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.

Handles API Request CouponPriceGroupList_Load_Query. 
Scope: Store.
:see: https://docs.miva.com/json-api/functions/couponpricegrouplist_load_query
"""

import merchantapi.abstract
import merchantapi.model
import merchantapi.response
from merchantapi.request import PriceGroupListLoadQuery
from merchantapi.client import BaseClient as Client
from requests.models import Response as HttpResponse


class CouponPriceGroupListLoadQuery(PriceGroupListLoadQuery):
	def __init__(self, client: Client = None, coupon: merchantapi.model.Coupon = None):
		"""
		CouponPriceGroupListLoadQuery Constructor.

		:param client: Client
		:param coupon: Coupon
		"""

		super().__init__(client)
		self.coupon_id = None
		self.edit_coupon = None
		self.coupon_code = None
		self.assigned = None
		self.unassigned = None
		if isinstance(coupon, merchantapi.model.Coupon):
			if coupon.get_id():
				self.set_coupon_id(coupon.get_id())
			elif coupon.get_code():
				self.set_edit_coupon(coupon.get_code())

	def get_function(self):
		"""
		Get the function of the request.

		:returns: str
		"""

		return 'CouponPriceGroupList_Load_Query'

	def get_coupon_id(self) -> int:
		"""
		Get Coupon_ID.

		:returns: int
		"""

		return self.coupon_id

	def get_edit_coupon(self) -> str:
		"""
		Get Edit_Coupon.

		:returns: str
		"""

		return self.edit_coupon

	def get_coupon_code(self) -> str:
		"""
		Get Coupon_Code.

		:returns: str
		"""

		return self.coupon_code

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

	def set_coupon_id(self, coupon_id: int) -> 'CouponPriceGroupListLoadQuery':
		"""
		Set Coupon_ID.

		:param coupon_id: int
		:returns: CouponPriceGroupListLoadQuery
		"""

		self.coupon_id = coupon_id
		return self

	def set_edit_coupon(self, edit_coupon: str) -> 'CouponPriceGroupListLoadQuery':
		"""
		Set Edit_Coupon.

		:param edit_coupon: str
		:returns: CouponPriceGroupListLoadQuery
		"""

		self.edit_coupon = edit_coupon
		return self

	def set_coupon_code(self, coupon_code: str) -> 'CouponPriceGroupListLoadQuery':
		"""
		Set Coupon_Code.

		:param coupon_code: str
		:returns: CouponPriceGroupListLoadQuery
		"""

		self.coupon_code = coupon_code
		return self

	def set_assigned(self, assigned: bool) -> 'CouponPriceGroupListLoadQuery':
		"""
		Set Assigned.

		:param assigned: bool
		:returns: CouponPriceGroupListLoadQuery
		"""

		self.assigned = assigned
		return self

	def set_unassigned(self, unassigned: bool) -> 'CouponPriceGroupListLoadQuery':
		"""
		Set Unassigned.

		:param unassigned: bool
		:returns: CouponPriceGroupListLoadQuery
		"""

		self.unassigned = unassigned
		return self

	# noinspection PyTypeChecker
	def send(self) -> 'merchantapi.response.CouponPriceGroupListLoadQuery':
		return super().send()

	def create_response(self, http_response: HttpResponse, data) -> 'CouponPriceGroupListLoadQuery':
		"""
		Create a response object from the response data

		:param http_response: requests.models.Response
		:param data:
		:returns: Response
		"""

		return merchantapi.response.CouponPriceGroupListLoadQuery(self, http_response, data)

	def to_dict(self) -> dict:
		"""
		Reduce the request to a dict

		:override:
		:returns: dict
		"""

		data = super().to_dict()

		if self.coupon_id is not None:
			data['Coupon_ID'] = self.coupon_id
		elif self.edit_coupon is not None:
			data['Edit_Coupon'] = self.edit_coupon
		elif self.coupon_code is not None:
			data['Coupon_Code'] = self.coupon_code

		if self.assigned is not None:
			data['Assigned'] = self.assigned
		if self.unassigned is not None:
			data['Unassigned'] = self.unassigned
		return data
