"""
This file is part of the MerchantAPI package.

(c) Miva Inc <https://www.miva.com/>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.
"""

from merchantapi.client import Client, ClientException
from merchantapi.request import OrderListLoadQuery

# Initialize a client
client = Client('https://www.mystore.com/mm5/json.mvc', 'MyApiToken', 'MySigningKey', {})

# Create a OrderListLoadQuery request instance, passing client to the constructor
request = OrderListLoadQuery(client)

# include additional order information by including ondemandcolumns
request.set_on_demand_columns([
  'ship_method',              # include the shipping method
  'cust_login',               # include the customers login
  'cust_pw_email',            # include the customers email address
  'business_title',           # include the customers business account title
  'payment_module',           # include the payment module information
  'customer',                 # include the customer information
  'items',                    # include the orders items
  'charges',                  # include the orders charges
  'coupons',                  # include the orders coupons
  'discounts',                # include the orders discounts
  'payments'                  # include the orders payments
])

# Include the orders notes
request.add_on_demand_column('notes')

# Include all custom fields
request.add_on_demand_column('CustomField_Values:*')

# Set the list sorting
request.set_sort('id', OrderListLoadQuery.SORT_DESCENDING)

# If you wish to decrypt payment data, you must provide the passphrase used by your encryption key
request.set_passphrase('MY_ENCRYPTION_KEYS_PASSPHRASE')

# Send the request
try:
	response = request.send()
except ClientException as e:
	print(str(e))

if not response.is_success():
	print('Error Loading Order List: %s: %s' % (response.get_error_code(), response.get_error_message()))
else:
	for order in response.get_orders():
		print('Order ID %d With %d Items, %d Charges Total %s' % (order.get_id(), len(order.get_items()), len(order.get_charges()), order.get_formatted_total()))
