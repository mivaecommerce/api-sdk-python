"""
This file is part of the MerchantAPI package.

(c) Miva Inc <https://www.miva.com/>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.
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

	# Multi call operation timeout, in seconds. Defaults to 60
	'operation_timeout': 60
}

client = Client('https://www.mystore.com/mm5/json.mvc', 'MyApiToken', 'MySigningKey', options)


'''
Authentication via SSH Private Key Signing
'''


from merchantapi.client import SSHClient
from merchantapi.authenticator import SSHPrivateKeyAuthenticator

client = SSHClient('https://www.mystore.com/mm5/json.mvc', 'Username', '/path/to/ssh/private/key/id_rsa', 'KeyPassword', SSHPrivateKeyAuthenticator.DIGEST_SSH_RSA_SHA256, options)

# Alternately, you can use a string value of the private

key = 'STRING_CONTENTS_OF_PRIVATE_KEY'

client = SSHClient('https://www.mystore.com/mm5/json.mvc', 'Username', '', '', SSHPrivateKeyAuthenticator.DIGEST_SSH_RSA_SHA256, options)
client.set_private_key_string(key, 'KeyPassword')


'''
Authentication via SSH Agent Signing
'''


from merchantapi.client import SSHAgentClient
from merchantapi.authenticator import SSHAgentAuthenticator

client = SSHAgentClient('https://www.mystore.com/mm5/json.mvc', 'Username', '/path/to/ssh/public/key/id_rsa.pub', SSHAgentAuthenticator.DIGEST_SSH_RSA_SHA256, options)

# Alternately, you can use a string value of the public key from the output of `ssh-add -L`

key = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDI7jEct+R0jfRTAH+OkBzv4kzgLIkfFBed9MG7FBPIuS5bZ134it+Cjkqmvb6DnH0bPumgDis9zrevIelg6UdLGAZnUt7qg8JjSjaGPCnZ5vlrcVO3PjeOlmnFUMl2g0eCFP9fdyXThwOFzrSrNlLMkngMtQ8yVlMcelmTq3LCm6Rt6c5ZJXIrTOV+msqUPKAOnYNcl2/ddTW5FuoH22p7kDDmZm1hjwCi2GXvgsmgOoXSqyRW0+52hOKiUOixLL3HUXyCrL9cKhcwwRdaK8lJKKAY3WGKHnwyFcoxgqy4Hg3KZRpjNEPasb0yt8E/tKFVKvpfnj0m7AjBHMhoj/PUJLZwY0/0a81Ua7ANGH73I7zDmRCYyHr0lJcAFeVI99t4t7/bmpEZBN9KVRbPEonkk331Z9jPj03aA+Kr9ZUgWgki1x3gJRsKgOOAtO75Zy1L9kn4iWIO/LdljQRCTVUY/3zyyaXztgKiR249Aw5LTrA+Kq+HdIGVNumhOjsc9t8= user@domain'
client = SSHAgentClient('https://www.mystore.com/mm5/json.mvc', 'Username', '', SSHAgentAuthenticator.DIGEST_SSH_RSA_SHA256, options)
client.set_public_key_string(key)


'''
Request Logging

Logging can be enabled by assigning a Logger instance to the client

Currently, we provide two logger types:
    FileLogger - logs to a local file
    ConsoleLogger - logs to std out/err
'''

from merchantapi.logging import FileLogger, ConsoleLogger

# Setting up a FileLogger
client.set_logger(FileLogger("/path/to/my/logfile.log"))

# Setting up a ConsoleLogger to log to stdout
client.set_logger(ConsoleLogger('stdout'))

# Setting up a ConsoleLogger to log to stderr
client.set_logger(ConsoleLogger('stderr'))
