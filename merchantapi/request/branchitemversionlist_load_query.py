"""
This file is part of the MerchantAPI package.

(c) Miva Inc <https://www.miva.com/>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.

Handles API Request BranchItemVersionList_Load_Query. 
Scope: Store.
:see: https://docs.miva.com/json-api/functions/branchitemversionlist_load_query
"""

import merchantapi.abstract
import merchantapi.model
import merchantapi.response
from merchantapi.listquery import ListQueryRequest
from merchantapi.client import BaseClient as Client
from requests.models import Response as HttpResponse


class BranchItemVersionListLoadQuery(ListQueryRequest):

	available_search_fields = [
		'id',
		'item_id',
		'user_id',
		'user_name',
		'code',
		'module_code',
		'module_name'
	]

	available_sort_fields = [
		'id',
		'item_id',
		'user_id',
		'user_name',
		'code',
		'module_id',
		'module_code',
		'module_name'
	]

	def __init__(self, client: Client = None, branch: merchantapi.model.Branch = None):
		"""
		BranchItemVersionListLoadQuery Constructor.

		:param client: Client
		:param branch: Branch
		"""

		super().__init__(client)
		self.branch_id = None
		self.edit_branch = None
		self.branch_name = None
		self.changeset_id = None
		if isinstance(branch, merchantapi.model.Branch):
			if branch.get_id():
				self.set_branch_id(branch.get_id())
			elif branch.get_name():
				self.set_edit_branch(branch.get_name())

	def get_function(self):
		"""
		Get the function of the request.

		:returns: str
		"""

		return 'BranchItemVersionList_Load_Query'

	def get_branch_id(self) -> int:
		"""
		Get Branch_ID.

		:returns: int
		"""

		return self.branch_id

	def get_edit_branch(self) -> str:
		"""
		Get Edit_Branch.

		:returns: str
		"""

		return self.edit_branch

	def get_branch_name(self) -> str:
		"""
		Get Branch_Name.

		:returns: str
		"""

		return self.branch_name

	def get_changeset_id(self) -> int:
		"""
		Get Changeset_ID.

		:returns: int
		"""

		return self.changeset_id

	def set_branch_id(self, branch_id: int) -> 'BranchItemVersionListLoadQuery':
		"""
		Set Branch_ID.

		:param branch_id: int
		:returns: BranchItemVersionListLoadQuery
		"""

		self.branch_id = branch_id
		return self

	def set_edit_branch(self, edit_branch: str) -> 'BranchItemVersionListLoadQuery':
		"""
		Set Edit_Branch.

		:param edit_branch: str
		:returns: BranchItemVersionListLoadQuery
		"""

		self.edit_branch = edit_branch
		return self

	def set_branch_name(self, branch_name: str) -> 'BranchItemVersionListLoadQuery':
		"""
		Set Branch_Name.

		:param branch_name: str
		:returns: BranchItemVersionListLoadQuery
		"""

		self.branch_name = branch_name
		return self

	def set_changeset_id(self, changeset_id: int) -> 'BranchItemVersionListLoadQuery':
		"""
		Set Changeset_ID.

		:param changeset_id: int
		:returns: BranchItemVersionListLoadQuery
		"""

		self.changeset_id = changeset_id
		return self

	# noinspection PyTypeChecker
	def send(self) -> 'merchantapi.response.BranchItemVersionListLoadQuery':
		return super().send()

	def create_response(self, http_response: HttpResponse, data) -> 'BranchItemVersionListLoadQuery':
		"""
		Create a response object from the response data

		:param http_response: requests.models.Response
		:param data:
		:returns: Response
		"""

		return merchantapi.response.BranchItemVersionListLoadQuery(self, http_response, data)

	def to_dict(self) -> dict:
		"""
		Reduce the request to a dict

		:override:
		:returns: dict
		"""

		data = super().to_dict()

		if self.branch_id is not None:
			data['Branch_ID'] = self.branch_id
		elif self.edit_branch is not None:
			data['Edit_Branch'] = self.edit_branch
		elif self.branch_name is not None:
			data['Branch_Name'] = self.branch_name

		return data
