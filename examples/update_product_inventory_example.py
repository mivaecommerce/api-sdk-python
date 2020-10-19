"""
This file is part of the MerchantAPI package.

(c) Miva Inc <https://www.miva.com/>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.
"""

from merchantapi.client import Client, ClientException
from merchantapi.request import ProductListAdjustInventory
from merchantapi.model import ProductInventoryAdjustment

# Initialize a client
client = Client('https://www.mystore.com/mm5/json.mvc', 'MyApiToken', 'MySigningKey', {})

# Create a ProductListAdjustInventory request instance, passing client to the constructor
request = ProductListAdjustInventory(client)

# Create instances of ProductInventoryAdjustment for each adjustment we want to make

# Add 100 to inventory count by product code
adjustment1 = ProductInventoryAdjustment()
adjustment1.set_product_code('PRODUCT_1').set_adjustment(100)

# Subtract 25 from inventory count by product code
adjustment2 = ProductInventoryAdjustment()
adjustment2.set_product_code('PRODUCT_2').set_adjustment(-25)

# Add 10 to inventory count by product id
adjustment3 = ProductInventoryAdjustment()
adjustment3.set_product_id(10248).set_adjustment(10)

# Add 30 to inventory count by product sku
adjustment4 = ProductInventoryAdjustment()
adjustment4.set_product_sku('ProductSku1').set_adjustment(30)

# Add the ProductInventoryAdjustment object to the Request
request.add_inventory_adjustment(adjustment1)

# You can also add an array of ProductInventoryAdjustment
request.add_inventory_adjustments([
	adjustment2,
	adjustment3,
	adjustment4
])

# Send the request
try:
	response = request.send()
except ClientException as e:
	print(str(e))
	exit()

if not response.is_success():
	print('Error Updating Product Inventory: %s: %s' % (response.get_error_code(), response.get_error_message()))
else:
	print('Successfully Updated Product Inventory')