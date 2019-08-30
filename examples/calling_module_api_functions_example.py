"""
This file is part of the MerchantAPI package.

(c) Miva Inc <https://www.miva.com/>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.

$Id: calling_module_api_functions_example.py 77672 2019-08-29 20:59:57Z gidriss $
"""

from merchantapi.client import Client, ClientException
from merchantapi.request import Module

# Initialize a client
client = Client('https://www.mystore.com/mm5/json.mvc', 'MyApiToken', 'MySigningKey', {})

# If you create a custom module or want to hook into an existing modules API functionality it exposes you can
# use the Module request class to call into the module.
request = Module(client)

request.set_module_code('MyModuleCode').set_module_function('MyModuleFunction')

# Add custom parameters to the request using the set_module_field method
request.set_module_field('MyModuleField', 'Foo').set_module_field('MyModuleField_Array', [
	'foo',
	'bar'
])

'''
It is best practice to create a custom class for your Module
by extending the Module or the Request class.
'''

# Send the request
try:
	response = request.send()

	if not response.is_success():
		print('Error: %s - %s' % (response.get_error_code(), response.get_error_message()))
	else:
		print('Success')
except ClientException as e:
	print(str(e))
