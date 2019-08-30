"""
This file is part of the MerchantAPI package.

(c) Miva Inc <https://www.miva.com/>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.

$Id: client_example.py 77671 2019-08-29 20:49:45Z gidriss $
"""

from merchantapi.client import Client

options = {
	#
	#    Boolean value designating if each request should include a
	#    timestamp or not. Default is true.
	#
	'require_timestamps': True,

	#    The signing digest type used for request signatures. Available
	#    options:
	#        Client.SIGN_DIGEST_SHA1
	#        Client.SIGN_DIGEST_SHA256
	#        Client.SIGN_DIGEST_NONE
	#
	#	defaults to Client.SIGN_DIGEST_SHA256

	'signing_key_digest': Client.SIGN_DIGEST_SHA256,
	#
	#  The default store code that will be added to each request that
	#  did not have one specified. Default is null.
	'default_store_code': 'STORE_CODE',

	# Enable or disable ssl verification. Default is True
	'ssl_verify': True
}

client = Client('https://www.mystore.com/mm5/json.mvc', 'MyApiToken', 'MySigningKey', options)
