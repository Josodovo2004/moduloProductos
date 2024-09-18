# from channels.generic.websocket import AsyncWebsocketConsumer
# import json
# from core.models import Item, ItemImpuesto, Catalogo05TiposTributos

# channelA = 'ModuloProductos_channel_a'

# class MyConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.channel_layer.group_add(
#             channelA,
#             self.channel_name
#         )
#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             channelA,
#             self.channel_name
#         )

#     async def recieve(self, event):
#         # Handle incoming messages
#         response_event = event.get('response_event')
#         serialized_items = event.get('items')

#         items_with_values = []

#         for item_data in serialized_items:
#             try:
#                 # Get the item and associated impuestos (taxes)
#                 item_id = item_data['id']
#                 item = Item.objects.get(id=item_id)
#                 impuestos = ItemImpuesto.objects.filter(item=item)

#                 # Initialize values
#                 valor_unitario = item.valorUnitario
#                 monto_total = 0
#                 monto_sin_impuestos = 0
#                 total_impuestos = 0
#                 impuesto_list = []

#                 # Calculate the total for the item
#                 monto_sin_impuestos = valor_unitario

#                 # Calculate the taxes (impuestos)
#                 for impuesto in impuestos:
#                     impuesto_data = {
#                         'id': impuesto.impuesto.codigo,
#                         'name': impuesto.impuesto.nombre,
#                         'tax_type_code': impuesto.impuesto.un_ece_5305,
#                     }

#                     # Calculate the tax amount
#                     impuesto_monto = (valor_unitario * impuesto.porcentaje) / 100
#                     total_impuestos += impuesto_monto

#                     # Add the calculated tax data
#                     impuesto_data['tax_amount'] = round(impuesto_monto, 2)
#                     impuesto_list.append(impuesto_data)

#                 # Total amount including taxes
#                 monto_total = monto_sin_impuestos + total_impuestos

#                 # Build the result for the item
#                 item_result = {
#                     'id': f'{item.codigoProducto}',
#                     'nombre': item.nombre,
#                     'currency': 'PEN',  # Assuming currency is PEN
#                     'total_amount': round(monto_total, 2),
#                     'tax_amount': round(total_impuestos, 2),
#                     'items': impuesto_list,
#                 }

#                 # Add the item to the result list
#                 items_with_values.append(item_result)

#             except Exception as e:
#                 # Handle any potential errors
#                 print(f"Error processing item {item_data['id']}: {str(e)}")
        
#         if response_event:
#             # Send response back
#             await self.channel_layer.send(
#                 'SistemaRV_channel_a',
#                 {
#                     'type': 'processItems',
#                     'processedItems': items_with_values,
#                     'response_event': response_event,
#                 }
#             )


# app2/consumers.py
from channels.generic.websocket import WebsocketConsumer
import json

class GreetingConsumer(WebsocketConsumer):
    def connect(self):
        self.channel_layer.group_add(
            'response_group',
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        self.channel_layer.group_discard(
            'response_group',
            self.channel_name
        )
