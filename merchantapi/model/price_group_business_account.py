"""
This file is part of the MerchantAPI package.

(c) Miva Inc <https://www.miva.com/>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.

PriceGroupBusinessAccount data model.
"""

from .business_account import BusinessAccount

class PriceGroupBusinessAccount(BusinessAccount):
	def __init__(self, data: dict = None):
		"""
		PriceGroupBusinessAccount Constructor

		:param data: dict
		"""

		super().__init__(data)

	def get_assigned(self) -> bool:
		"""
		Get assigned.

		:returns: bool
		"""

		return self.get_field('assigned', False)
