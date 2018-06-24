from django.db import models


# Create your models here.
from django.utils import timezone


class ProductGroup(models.Model):
    name = models.CharField(max_length=300, verbose_name='Наименование')

    created = models.DateTimeField(default=timezone.now, verbose_name='Создано')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Обновлено')

    def __str__(self):
        return self.name

    objects = models.Manager()

    class Meta:
        verbose_name = 'группа продуктов'
        verbose_name_plural = 'группы продуктов'


class Product(models.Model):
    name = models.CharField(max_length=300,
                            verbose_name='Наименование')

    price = models.FloatField(default=0,
                              verbose_name='Цена')

    group = models.ForeignKey(ProductGroup,
                              on_delete=models.CASCADE,
                              blank=True,
                              null=True,
                              verbose_name='Группа')

    weight = models.FloatField(default=0,
                               blank=True,
                               null=True,
                               verbose_name='Вес')

    length = models.FloatField(default=0,
                               blank=True,
                               null=True,
                               verbose_name='Длина')

    width = models.FloatField(default=0,
                              blank=True,
                              null=True,
                              verbose_name='Ширина')

    height = models.FloatField(default=0,
                               blank=True,
                               null=True,
                               verbose_name='Высота')

    created = models.DateTimeField(default=timezone.now, verbose_name='Создано')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Обновлено')

    def __str__(self):
        return self.name

    objects = models.Manager()

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
