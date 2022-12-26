from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Country(models.Model):
    title = models.CharField(max_length=15, verbose_name='Страна')

    def __str__(self):
        return self.title


class Factory(models.Model):
    title = models.CharField(max_length=17, verbose_name='Производитель')

    def __str__(self):
        return self.title


class Beer(models.Model):
    title = models.CharField(max_length=19, verbose_name='Название')
    manufacture = models.ForeignKey(Factory, on_delete=models.CASCADE, verbose_name='Завод', null=True, blank=True)
    volume = models.IntegerField(default=5, verbose_name='Крепость')
    type = models.CharField(max_length=12, blank=True, verbose_name='Тип')
    price = models.IntegerField(default=0, verbose_name='Цена')
    state = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Страна', null=True, blank=True)

    def __str__(self):
        return self.title


class Shop(models.Model):
    title = models.CharField(max_length=15, verbose_name='Название')
    products = models.ManyToManyField(Beer, null=True, blank=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Заказчик')
    title = models.ManyToManyField(Beer, null=True, blank=True)
    magazine = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True)

