"""
This file is part of the MerchantAPI package.

(c) Miva Inc <https://www.miva.com/>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.

Handles API Request AttributeTemplateAttributeList_Load_Query. 
Scope: Store.
:see: https://docs.miva.com/json-api/functions/attributetemplateattributelist_load_query
"""

import merchantapi.abstract
import merchantapi.model
import merchantapi.response
from merchantapi.listquery import ListQueryRequest
from merchantapi.client import BaseClient as Client
from requests.models import Response as HttpResponse


class AttributeTemplateAttributeListLoadQuery(ListQueryRequest):

	available_search_fields = [
		'id',
		'attr_code',
		'attr_prompt',
		'attr_price',
		'attr_cost',
		'attr_weight',
		'attr_image',
		'opt_code',
		'opt_prompt',
		'opt_price',
		'opt_cost',
		'opt_weight',
		'opt_image',
		'code',
		'prompt',
		'price',
		'cost',
		'weight',
		'image',
		'required',
		'inventory'
	]

	available_sort_fields = [
		'id',
		'code',
		'type',
		'prompt',
		'price',
		'cost',
		'weight',
		'image',
		'required',
		'inventory',
		'attr_code',
		'attr_prompt',
		'attr_price',
		'attr_cost',
		'attr_weight',
		'attr_image',
		'opt_code',
		'opt_prompt',
		'opt_price',
		'opt_cost',
		'opt_weight',
		'opt_image'
	]

	def __init__(self, client: Client = None, attribute_template: merchantapi.model.AttributeTemplate = None):
		"""
		AttributeTemplateAttributeListLoadQuery Constructor.

		:param client: Client
		:param attribute_template: AttributeTemplate
		"""

		super().__init__(client)
		self.attribute_template_id = None
		self.attribute_template_code = None
		self.edit_attribute_template = None
		if isinstance(attribute_template, merchantapi.model.AttributeTemplate):
			if attribute_template.get_id():
				self.set_attribute_template_id(attribute_template.get_id())
			elif attribute_template.get_code():
				self.set_attribute_template_code(attribute_template.get_code())
			elif attribute_template.get_code():
				self.set_edit_attribute_template(attribute_template.get_code())

	def get_function(self):
		"""
		Get the function of the request.

		:returns: str
		"""

		return 'AttributeTemplateAttributeList_Load_Query'

	def get_attribute_template_id(self) -> int:
		"""
		Get AttributeTemplate_ID.

		:returns: int
		"""

		return self.attribute_template_id

	def get_attribute_template_code(self) -> str:
		"""
		Get AttributeTemplate_Code.

		:returns: str
		"""

		return self.attribute_template_code

	def get_edit_attribute_template(self) -> str:
		"""
		Get Edit_AttributeTemplate.

		:returns: str
		"""

		return self.edit_attribute_template

	def set_attribute_template_id(self, attribute_template_id: int) -> 'AttributeTemplateAttributeListLoadQuery':
		"""
		Set AttributeTemplate_ID.

		:param attribute_template_id: int
		:returns: AttributeTemplateAttributeListLoadQuery
		"""

		self.attribute_template_id = attribute_template_id
		return self

	def set_attribute_template_code(self, attribute_template_code: str) -> 'AttributeTemplateAttributeListLoadQuery':
		"""
		Set AttributeTemplate_Code.

		:param attribute_template_code: str
		:returns: AttributeTemplateAttributeListLoadQuery
		"""

		self.attribute_template_code = attribute_template_code
		return self

	def set_edit_attribute_template(self, edit_attribute_template: str) -> 'AttributeTemplateAttributeListLoadQuery':
		"""
		Set Edit_AttributeTemplate.

		:param edit_attribute_template: str
		:returns: AttributeTemplateAttributeListLoadQuery
		"""

		self.edit_attribute_template = edit_attribute_template
		return self

	# noinspection PyTypeChecker
	def send(self) -> 'merchantapi.response.AttributeTemplateAttributeListLoadQuery':
		return super().send()

	def create_response(self, http_response: HttpResponse, data) -> 'AttributeTemplateAttributeListLoadQuery':
		"""
		Create a response object from the response data

		:param http_response: requests.models.Response
		:param data:
		:returns: Response
		"""

		return merchantapi.response.AttributeTemplateAttributeListLoadQuery(self, http_response, data)

	def to_dict(self) -> dict:
		"""
		Reduce the request to a dict

		:override:
		:returns: dict
		"""

		data = super().to_dict()

		if self.attribute_template_id is not None:
			data['AttributeTemplate_ID'] = self.attribute_template_id
		elif self.attribute_template_code is not None:
			data['AttributeTemplate_Code'] = self.attribute_template_code
		elif self.edit_attribute_template is not None:
			data['Edit_AttributeTemplate'] = self.edit_attribute_template

		return data
