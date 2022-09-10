from django.db import models
from django.contrib.auth.models import User
from clients.models import Order

# clients/models.py


class Bottle(models.Model):
    volume = models.IntegerField(default=10)
    maker = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    expired = models.BooleanField(default=False)

    orders = models.ManyToManyField(
        to=Order,
        null=True, blank=True,
        verbose_name='Заказы',
        related_name='bottles'
    )


class Client(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.SET_NULL, null=True, blank=True, related_name='client')
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    bottles_ordered = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(verbose_name='Фото',
                              upload_to='photos',
                              null=True,
                              blank=True)


class Order(models.Model):

    client = models.ForeignKey(
        to=Client, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='order'
    )
    created_at = models.DateTimeField(verbose_name='Дата и время создания заказа',
                                      auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата и время изменения заказа',
                                      auto_now=True)
    description = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=250)
    contacts = models.CharField(max_length=250)
    finished = models.BooleanField(default=False)


class BottleCount(models.Model):
    count = models.IntegerField(default=0)

    order = models.ManyToOneRel(
        to=Order,
        null=True, blank=True,
        verbose_name='Заказы,',
        related_name='bottles'
    )

    bottle = models.ManyToOneRel(
        to=Bottle,
        null=True, blank=True,
        verbose_name='Количество бутылок',
        related_name='orders'
    )


def __str__(self):
    return f'{self.name} - {self.contacts}'


class Meta:
    verbose_name = 'Заказ'
    verbose_name_plural = 'Заказы'
