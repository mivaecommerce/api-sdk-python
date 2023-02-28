"""
This file is part of the MerchantAPI package.

(c) Miva Inc <https://www.miva.com/>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.
"""

from merchantapi.client import Client, ClientException
from merchantapi.request import ProductListLoadQuery
from merchantapi.listquery import FilterExpression

# Initialize a client
client = Client('https://www.mystore.com/mm5/json.mvc', 'MyApiToken', 'MySigningKey', {})

'''
All Request objects which inherit from ListQueryRequest
can utilize the FilterExpression class to fluently add
search filters to the *List_Load_Query requests.
:see: ListQueryRequest in listquery.py
:see: FilterExpression in listquery.py
'''

request = ProductListLoadQuery(client)

'''
You can filter list load query requests with FilterExpressions.
ListQueryRequest classes all have a default filter expression.
You can access it with the get_filters() method.
This will enforce only adding search filters to
defined fields in ProductListLoadQuery. Trying to
filter against undefined fields throws an exception.

:see: ProductListLoadQuery::available_search_fields
:see: ProductListLoadQuery::get_available_search_fields()
:see: FilterExpression
'''

filters = request.get_filters()

'''
Alternately, you can just create a FilterExpression object
with request.filter_expression(), just be sure to set it
with request.set_filters(filters).

And finally, you can just create a FilterExpression object
directly.

	filters = FilterExpression()

This will not enforce a requests available search fields.

	filters = FilterExpression(request)

This will enforce a requests available search fields.
'''

filters.equal('code', 'foo').or_equal('code', 'bar')

# You can nest additional expressions to create
# more complex search queries:

filters.or_x(
	filters.expr().like('code', 'BAZ%').and_greater_than('price', 9.99)
)


'''
This would result in a query along the lines of:
	[...] WHERE code = 'foo' OR code = 'bar' OR ( code LIKE 'BAZ%' AND price > 9.99 )
'''

# You can get an array of available search fields for a ListQueryRequest
available_search_fields = request.get_available_search_fields()

# You can also just supply a custom array of list filters you wish to apply
request.set_filters([
	{
		'name': 'search',
		'value': {
			'field': 'code',
			'operator': 'EQ',
			'value': 'Foo'
		}
	},
	{
		'name': 'search_AND',
		'value': {
			'field': 'price',
			'operator': 'GT',
			'value': 9.99
		}
	}
])


# Some *List_Load_Query functions allow you to include additional data in the response
# by specifying additional on demand columns

# You can add a single column
request.add_on_demand_column('column')

# You can set (and replace) an array columns
request.set_on_demand_columns(['column', 'column2', 'column3'])

# You can get an array of supported columns from the Request
available_columns = request.get_available_on_demand_columns()

# You can set all supported on demand columns the request supports like this
request.set_on_demand_columns(request.get_available_on_demand_columns())

# Lists which include Custom Fields (Product,Category,Order) you must explicitly specify
# the custom field module and code as an on demand column or using wildcards

# Includes ALL custom fields
request.add_on_demand_column('CustomField_Values:*')

# Includes all fields provided by the customfields module
request.add_on_demand_column('CustomField_Values:customfields:*')

# includes only the MyFieldCode provided by the customfields module
request.add_on_demand_column('CustomField_Values:customfields:MyFieldCode')

# You can sort the result list by using  the setSort method on the Request
request.set_sort('field', ProductListLoadQuery.SORT_DESCENDING)

# Get an array of available sort fields
available_sort_fields = request.get_available_sort_fields()

# Some *List_Load_Query functions support custom filters specific to the request.
# You can add custom filters using the setCustomFilter method. The value type will
# vary for each custom field.

request.set_custom_filter('Custom_Filter_Name', 'Custom_Filter_Value')

try:
	response = request.send()
except ClientException as e:
	print(str(e))
	exit()

if response.is_error():
	print('Load Products Error: %s: %s' % (response.get_error_code(), response.get_error_message()))
else:
	for product in response.get_products():
		print('Product ID: %d Code: %s Name: %s' % (product.get_id(),  product.get_code(),  product.get_name()))

	# Custom Field Values can be accessed via the CustomFieldValues model object
	# :see: CustomFieldValues

	my_custom_field = product.get_custom_field_values().get_value('MyFieldCode')
	my_module_custom_field = product.get_custom_field_values().get_value('MyModuleFieldCode', 'MyModule')
