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
