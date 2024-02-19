from django.apps import AppConfig


# FIXME: if new ddbb, should comment this function, because would not have make querys here
def checkToken():
    import requests
    from .models import Tokens
    from datetime import datetime, timezone, timedelta

    if not Tokens.objects.all():
        print('NOT TOKEN')
        Tokens.objects.create(token="APP_USR-715970904874422-122216-37d33ac5c704c3e19c59c6749d0533d7-117331702",
                              refresh_token="TG-6585f1c3e19b430001635f57-117331702")

    tokens_obj = Tokens.objects.get(id=1)
    # tokens_obj.token = "APP_USR-715970904874422-122216-37d33ac5c704c3e19c59c6749d0533d7-117331702"
    # .refresh_token = "TG-6585f1c3e19b430001635f57-117331702"
    # tokens_obj.save()
    refresh_token = tokens_obj.refresh_token

    now = datetime.now(timezone.utc)
    diference = now - tokens_obj.last_update
    time_to_refresh = timedelta(days=0, hours=6, minutes=0)

    if diference > time_to_refresh:
        try:
            url = "https://api.mercadolibre.com/oauth/token"
            payload = 'grant_type=refresh_token&client_id=715970904874422&client_secret=SakB6qmXU9r5ONukgos7RYHhNwSaNVsX&refresh_token=' + refresh_token
            headers = {
                'accept': 'application/json',
                'content-type': 'application/x-www-form-urlencoded'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            print("** RESPONSE ON TRY REFRESH TOKEN: ")
            print(response.text)
            if response:
                print("NEW TOKEN RESPONSE: ")
                print(response.json())
                tokens_obj.token = response.json()['access_token']
                tokens_obj.refresh_token = response.json()['refresh_token']
                tokens_obj.save()
        except Exception as e:
            print("ERROR al intentar resfrescar token API Mercadolibre: ")
            print(e)


def getOrders():
    
    import requests
    import json
    from .models import Order, Tokens
    from datetime import datetime

    checkToken()  # Critical HEAVY-TON

    token_obj = Tokens.objects.get(id=1)
    token = token_obj.token

    # Build and Make ORDERS request
    url = "https://api.mercadolibre.com/orders/search?seller=117331702&sort=date_desc"
    payload = {}
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 401:
        print("custom ERROR : Sin respuesta al solicitar ordenes API ML")
        return "NOT_UPDATED"

    orders_resp = json.loads(response.text)['results']

    local_orders_ids = list(Order.objects.values_list('order_id', flat=True))

    for order in orders_resp:
        first_product = order['order_items'][0]

        if str(order['id']) not in local_orders_ids:
            date_ml = order['date_closed']
            format = "%Y-%m-%d,%H:%M:%S"
            string_date = ','.join([date_ml.split('T')[:1][0], date_ml[11:19]])
            dt_object = datetime.strptime(string_date, format)

            # Consulta receptor (Imposible saber nombre del comprador)
            url = "https://api.mercadolibre.com/shipments/" + str(order['shipping']['id'])
            payload = {}
            headers = {'Authorization': 'Bearer ' + token}
            response = requests.request("GET", url, headers=headers, data=payload)
            detalle_envio = json.loads(response.text)
            recibe_name = detalle_envio['receiver_address']['receiver_name']

            # FIXME for possible muliple products
            data = {
                'order_id': order['id'],
                'product': first_product['item']['seller_sku'] or first_product['item']['title'],
                'customer': recibe_name or 'USER_NOT_AVAILABLE',
                'unit_price': first_product['unit_price'],
                'qty': first_product['quantity'],
                'subtotal': order['total_amount'],
                'total': order['total_amount'],
                'date': order['date_created'],
                'notas': "Venta #" + str(order['id']) + ' - ' + str(dt_object.day) + " "
                         + str(dt_object.strftime("%B") + ' ' + str(dt_object.year)) + "   /   "
                         + 'Usuario: ' + order['buyer']['nickname'],
                'status': order['status']  # paid
            }
            new_order_obj = Order.objects.create(**data)
            new_order_obj.save()
    return "OK"


class InventarioConfig(AppConfig):
    name = 'inventario'
    verbose_name = "Aplicacion inventario y administracion de ventas"

    def ready(self):
        getOrders()

