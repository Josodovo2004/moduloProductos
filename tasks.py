from celery import shared_task # type: ignore
from core.models import Item, ItemImpuesto
from core.serializers import ItemSerializer, ItemImpuestoSerializer

@shared_task
def darvaloresDeItems(serialized_items):
    # Initialize the result dictionary
    items_with_values = []

    for item_data in serialized_items:
        try:
            # Get the item and associated impuestos (taxes)
            item_id = item_data['id']
            cantidad = item_data['cantidad']
            item = Item.objects.get(id=item_id)
            impuestos = ItemImpuesto.objects.filter(item=item)

            # Initialize values
            valor_unitario = item.valorUnitario
            monto_total = 0
            monto_sin_impuestos = 0
            total_impuestos = 0
            impuesto_list = []

            # Calculate the total for the item
            monto_sin_impuestos = valor_unitario * cantidad

            # Calculate the taxes (impuestos)
            for impuesto in impuestos:
                impuesto_data = {
                    'id': impuesto.impuesto.codigo,
                    'name': impuesto.impuesto.nombre,
                    'tax_type_code': impuesto.impuesto.un_ece_5305,
                }

                # Calculate the tax amount
                impuesto_monto = (monto_sin_impuestos * impuesto.porcentaje)
                total_impuestos += impuesto_monto

                # Add the calculated tax data
                impuesto_data['tax_amount'] = round(impuesto_monto, 2)
                impuesto_list.append(impuesto_data)

            # Total amount including taxes
            monto_total = monto_sin_impuestos + total_impuestos

            # Build the result for the item
            item_result = {
                'total_amount': round(monto_total, 2),
                'paid_amount': round(monto_sin_impuestos, 2),
                'tax_amount': round(total_impuestos, 2),
                'items': impuesto_list,
            }

            # Add the item to the result list
            items_with_values.append(item_result)

        except Exception as e:
            # Handle any potential errors
            print(f"Error processing item {item_data['id']}: {str(e)}")

    # Return the final calculated list of items with values
    return items_with_values