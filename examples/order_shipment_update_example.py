"""
This file is part of the MerchantAPI package.

(c) Miva Inc <https://www.miva.com/>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.
"""

'''
This example will load an order by its ID from the first argument passed to it when run 
then proceed to create a shipment for all items in the order and then finally update the shipment
with tracking information and mark it as shipped.
'''

import sys
import time
from merchantapi.client import Client, ClientException
from merchantapi.request import OrderListLoadQuery, OrderShipmentListUpdate, OrderItemListCreateShipment
from merchantapi.model import OrderShipmentUpdate

# Initialize a client
client = Client('https://www.mystore.com/mm5/json.mvc', 'MyApiToken', 'MySigningKey', {})

order_request = OrderListLoadQuery(client)

order_request.get_filters().equal('id', sys.argv[1])

order_response = order_request.send()

if not order_response.is_success():
  print('Error Loading Order List: %s: %s' % (order_response.get_error_code(), order_response.get_error_message()))
  quit()

for order in order_response.get_orders():
  if not len(order.get_items()):
    continue

  # Create a shipment for all items in the order

  create_shipment_request = OrderItemListCreateShipment(client)

  for item in order.get_items():
    if item.get_shipment_id() > 0:
      continue # Skip items that are already in a shipment

    create_shipment_request.add_order_item(item)

  create_shipment_response = create_shipment_request.send()
  
  if not create_shipment_response.is_success():
    print('Error Creating Order Shipment: %s: %s' % (create_shipment_response.get_error_code(), create_shipment_response.get_error_message()))
    quit()


  shipment = create_shipment_response.get_shipment()

  # Now that we have created a shipment for the items in the order we can
  # assign a tracking number and mark it shipped

  shipment_update_request = OrderShipmentListUpdate(client)
  shipment_update = OrderShipmentUpdate()
  tracking_number = 'Z%s' % time.time()

  shipment_update.set_cost(1.00)
  shipment_update.set_mark_shipped(True)
  shipment_update.set_shipment_id(shipment.get_id())
  shipment_update.set_tracking_number(tracking_number)
  shipment_update.set_tracking_type('UPS')

  shipment_update_request.add_shipment_update(shipment_update)

  shipment_update_response = shipment_update_request.send()

  if not shipment_update_response.is_success():
    print('Error Updating Order Shipment: %s: %s' % (shipment_update_response.get_error_code(), shipment_update_response.get_error_message()))
    quit()

  print 'Order %d Shipment %d Updated With Tracking %s' % (order.get_id(), shipment.get_id(), tracking_number)
