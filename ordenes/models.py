from django.db import models
from django.urls import reverse
from datetime import datetime, timezone
from model_utils import Choices


# Para el acceso a las ordenes de Meli
class Tokens(models.Model):
    token = models.CharField(max_length=250)
    refresh_token = models.CharField(max_length=250)
    is_update = models.BooleanField(default=False)
    last_update = models.DateTimeField(default=datetime.now(timezone.utc))


class Order(models.Model):
    STATUSES = Choices((1, 'procesando'), (2, 'entregado'), (3, 'cancelado'))
    # Todo: product deberia cambiarse por products m2m.
    order_id = models.CharField(max_length=250, default='NA')
    product = models.CharField(max_length=250, default=None, null=True)
    customer = models.CharField(max_length=250, default='NA')  # TODO : default value is not work? why?
    unit_price = models.FloatField(default=0.0)
    qty = models.IntegerField(default=0)
    subtotal = models.FloatField(default=0.0)
    total = models.FloatField(default=0.0)
    date = models.CharField(max_length=250, default='NA')
    status = models.CharField(max_length=250, default='NA')
    notas = models.CharField(max_length=250, default='NA', db_index=True,)
