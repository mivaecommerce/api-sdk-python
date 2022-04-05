"""
This file is part of the MerchantAPI package.

(c) Miva Inc <https://www.miva.com/>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.
"""

from merchantapi.client import Client, ClientException
from merchantapi.request import CustomerAddressListLoadQuery, CustomerPaymentCardRegister, SubscriptionShippingMethodListLoadQuery, SubscriptionInsert
from merchantapi.model import SubscriptionAttribute
import time
import datetime

# Initialize a client

client = Client('https://www.mystore.com/mm5/json.mvc', 'MyApiToken', 'MySigningKey', {})

product_code = 'MySubscriptionProduct'
product_subscription_term = 'MySubscriptionTermDescription'
customer_login = 'CustomerLogin'

try:
	#
	# Load our subscribing customers addresses
	#

	address_request = CustomerAddressListLoadQuery(client)

	address_request.set_customer_login(customer_login)

	address_response = address_request.send()

	if not address_response.is_success():
		print('Error Loading Addresses: %s - %s' % (address_response.get_error_code(), address_response.get_error_message()))
		return
	elif not len(address_response.get_customer_addresses()):
		print('Address not found')
		return

	address = address_response.get_customer_addresses()[0]

	#
	# Register a payment card with CustmerPaymentCardRegisterRequest
	# Or load an existing card with CustomerPaymentCardListLoadQueryRequest
	# In this example we are going to register a payment card
	#

	payment_card_request = CustomerPaymentCardRegister(client)

	payment_card_request.set_customer_login(customer_login)
    payment_card_request.set_first_name(address.get_first_name())
    payment_card_request.set_last_name(address.get_last_name())
    payment_card_request.set_card_type('Visa')
    payment_card_request.set_card_number('4111111111111111')
    payment_card_request.set_expiration_month(08)
    payment_card_request.set_expiration_year(2025)
    payment_card_request.set_address1(address.get_address1())
    payment_card_request.set_address2(address.get_address2())
    payment_card_request.set_city(address.get_city())
    payment_card_request.set_state(address.get_state())
    payment_card_request.set_zip(address.get_zip())
    payment_card_request.set_country(address.get_country())
	
	payment_card_response = payment_card_request.send()

	if not payment_card_response.is_success():
		print('Error Registering Payment Card: %s - %s' % (payment_card_response.get_error_code(), payment_card_response.get_error_message()))
		return

	payment_card = payment_card_response.get_customer_payment_card()

	#
	# Find a valid shipping method
	#
	
	method_request = SubscriptionShippingMethodListLoadQuery(client)

	method_request.set_product_code(product_code)
	method_request.set_product_subscription_term_description(product_subscription_term)
	method_request.set_customer_login(customer_login)
	method_request.set_address_id(address.get_id())
	method_request.set_payment_card_id(payment_card.get_id())
	method_request.set_quantity(1)

	method_response = method_request.send()

	if not method_response.is_success():
		print('Error Loading Shipping Methods: %s - %s' % (method_response.get_error_code(), method_response.get_error_message()))
		return
	elif not len(method_response.get_subscription_shipping_methods()):
		print('Shipping method not found')
		return

	method = method_response.get_subscription_shipping_methods()[0]

	#
	# Create the subscription
	#
    
    request = SubscriptionInsert(client)
    
    request.set_product_code(product_code)
    request.set_product_subscription_term_description(product_subscription_term)
    request.set_customer_login(customer_login)
    request.set_customer_address_id(address.get_id())
    request.set_payment_card_id(payment_card.get_id())
    request.set_quantity(1)
    request.set_ship_id(method.get_module().get_id())							# Supply the shipping module id
    request.set_ship_data("MyShippingMethodData")     							# Supply any required shipping data for this method
	request.set_next_date(int(time.mktime(datetime.date.today().timetuple())))	# Set the next charge date, in this case we are using today

	response = request.send()

	if not response.is_success():
		print('Error Creating Subscription: %s - %s' % (response.get_error_code(), response.get_error_message()))
		return

	print('Created Subscription %d Customer %s Product %s Term %s' % (response.get_subscription().get_id(), customer_login, product_code, product_subscription_term))
except ClientException as e:
	print(str(e))