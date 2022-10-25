# Upgrade Guide from 2.1.0 to 2.2.0

Issue **MMAPI-62** added the inserted object into the response. ProductVariantInsertResponse has had its original response data moved and all calling code should be updated to reflect this change.

***Example usage from 2.1.x***

	response.get_product_id();
	response.get_variant_id();

***Should be updated to for 2.2.x***
	
	response.getProductVariant().getProductId()
	response.getProductVariant().getVariantId()

Issue **MMAPI-67** renamed some model getter functions and all calling code should be updated. Use the following list to rename all usage in your applications:

	CustomerSubscription.get_adress_descrip() 		-> CustomerSubscription.get_address_description()
	CustomerSubscription.get_address_adress() 		-> CustomerSubscription.get_address_address()
	CustomerSubscription.get_address_address_1()	-> CustomerSubscription.get_address_address1()
	CustomerSubscription.get_address_address_2()	-> CustomerSubscription.get_address_address2()
	ProductAndSubscriptionTerm.get_term_descrip()	-> ProductAndSubscriptionTerm.get_term_description()

# Upgrade Guide from 2.0.X - 2.1.0+

The class `TemplateVersionSettings` has been renamed to `VersionSettings`.

If you are utilizing this class within your code then you will need to be renamed in their type declarations. Usage has stayed the same.

# Upgrade Guide from 1.x to 2.x

## New Dependencies

After updating, be sure to install the new required dependencies `cryptography` and `bcrypt`:

   pip install -r requirements.txt

## Usage of OrderItemOption

Usage of OrderItemOption will need to be updated to support the change to the member `attribute` to `attribute_code`.

Replace all usage of `OrderItemOption` models that call either `get_attribute()` or `set_attribute(str)` with `get_attribute_code()` and `set_attribute_code(str)`.

**Example usage from 1.x:**

    item_option = merchantapi.model.OrderItemOption()
    item_option.set_attribute('code')

**Should be updated for 2.x:**

    item_option = merchantapi.model.OrderItemOption()
    item_option.set_attribute_code('code')

**Example usage from 1.x:**

	item_option; // A OrderItemOption model loaded from an OrderListLoadQuery, for example
	item_option.get_attribute();

**Should be updated for 2.x:**

	var item_option; // A OrderItemOption model loaded from an OrderListLoadQuery, for example
	item_option.get_attribute_code();
