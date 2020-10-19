"""
This file is part of the MerchantAPI package.

(c) Miva Inc <https://www.miva.com/>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.
"""

from merchantapi.client import Client, ClientException
from merchantapi.request import ProductListLoadQuery, ProductUpdate

# Initialize a client
client = Client('https://www.mystore.com/mm5/json.mvc', 'MyApiToken', 'MySigningKey', {})


# Load the product first
productrequest = ProductListLoadQuery(client)

# apply filtering to match a specific product
# :see: list_query_example.js

productrequest.set_filters(
  productrequest.filter_expression().equal('code', 'MY_PRODUCT')
)

try:
	productresponse = productrequest.send()
except ClientException as e:
	print(str(e))

if not productresponse.is_success():
	print('Load Product Error: %s: %s' % (productresponse.get_error_code(), productresponse.get_error_message()))
	exit()
elif not len(productresponse.get_products()):
	print('Product Not Found')
	exit()

product = productresponse.get_products()[0]

print('Loaded Product %s Code %s Name %s' % (product.get_id(), product.get_code(), product.get_name()))

'''
Some requests accept a Model object in their constructor
which will allow the Request object to inherit data from.
ProductUpdate accepts a Product model.
'''

request = ProductUpdate(client, product)

request.set_product_name('The New Product Name')
request.set_product_description('New Product Description')
request.set_product_price(39.99)
request.set_product_cost(29.99)
request.set_product_weight(2.5)

response = request.send()

if not response.is_success():
	print('Load Product Error: %s: %s' % (response.get_error_code(), response.get_error_message()))
else:
	print('Product Updated')
