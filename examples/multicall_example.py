"""
This file is part of the MerchantAPI package.

(c) Miva Inc <https://www.miva.com/>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.

$Id: multicall_example.py 77672 2019-08-29 20:59:57Z gidriss $
"""

from merchantapi.client import Client, ClientException
from merchantapi.request import ProductUpdate
from merchantapi.request import ProductListLoadQuery
from merchantapi.request import CategoryListLoadQuery
from merchantapi.request import PriceGroupListLoadQuery
from merchantapi.multicall import MultiCallRequest

# Initialize a client
client = Client('https://www.mystore.com/mm5/json.mvc', 'MyApiToken', 'MySigningKey', {})

# Create a MultiCallRequest and add Request objects to it
request = MultiCallRequest(client)

request.add_request(ProductListLoadQuery())

request.add_requests([
	CategoryListLoadQuery(),
	PriceGroupListLoadQuery()
])

# Send the request
try:
	response = request.send()
except ClientException as e:
	print(str(e))
	exit()

if not response.is_success():
	print('Error Executing MultiCallRequest: %s: %s' % (response.get_error_code(), response.get_error_message()))
else:
	for r in response.get_responses():
		print('Response for %s' % (r.get_function()))
		print(r.get_data())

'''
Utilizing the Iterations feature allows you to compact request
data by grouping multiple iterations to the same API function
in sequence.

:see: MultiCallOperation
'''

request = MultiCallRequest(client)

# Create a new MultiCallOperation and adds it to the Request.
operation = request.operation()

'''
	Alternately:
		from merchantapi.multicall import MultiCallOperation
		operation = MultiCallOperation()
		...
		request.add_operation(operation)
'''

'''
Set shared data between the iterations, for example we can set a shared
value for Product_Price and update many products without specifying the same
data for each of the iterations.
'''

operation.add_shared_data('Product_Price', 29.99)

'''
Or set the shared data dict:
	operation.set_shared_data({ 'Product_Price': 29.99 })
'''

# We now add all the same request types to the operation to make use of iterations

update1 = ProductUpdate(client)

update1.set_edit_product('PROD_1')

update2 = ProductUpdate(client)

update2.set_edit_product('PROD_2')

update3 = ProductUpdate(client)

update3.set_edit_product('PROD_3')

update4 = ProductUpdate(client)

update4.set_edit_product('PROD_4').set_product_name('Product 4')

operation.add_request(update1)
operation.add_request(update2)
operation.add_request(update3)
operation.add_request(update4)

# We can add more requests as well. Add a Product List Load to get the updated products at the end
checkproducts = ProductListLoadQuery(client)

checkproducts.set_filters(
	checkproducts.filter_expression().is_in('code', ['PROD_1', 'PROD_2', 'PROD_3', 'PROD_4'])
)

request.add_request(checkproducts)

# Send the request
try:
	response = request.send()
except ClientException as e:
	print(str(e))
	exit()

if not response.is_success():
	print('Error Executing MultiCallRequest: %s: %s' % (response.get_error_code(), response.get_error_message()))
else:
	for r in response.get_responses():
		print('Response for %s' % r.get_request().get_function())
		print(r.get_data())
