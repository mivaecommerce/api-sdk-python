"""
This file is part of the MerchantAPI package.

(c) Miva Inc <https://www.miva.com/>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.
"""

from merchantapi.client import Client, ClientException
from merchantapi.request import ProductInsert

# Initialize a client
client = Client('https://www.mystore.com/mm5/json.mvc', 'MyApiToken', 'MySigningKey', {})

# Create a ProductInsert request instance, passing client to the constructor
request = ProductInsert(client)

# Setup our request variables */
request.set_product_code('NEW_PRODUCT')
request.set_product_name('My New Product')
request.set_product_price(29.99)
request.set_product_weight(1.5)

# Send the request
try:
	response = request.send()

	if response.is_success():
		print('Successfully Inserted Product')
	else:
		print('Error Inserting Product: %s - %s' % (response.get_error_code(), response.get_error_message()))
except ClientException as e:
	print(str(e))
