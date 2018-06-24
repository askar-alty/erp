from django.db import models

# Create your models here.
from django.utils import timezone


class IncomeItemGroup(models.Model):
    name = models.CharField(max_length=300,
                            verbose_name='Нименование')

    created = models.DateTimeField(default=timezone.now, verbose_name='Создано')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Обновлено')

    def __str__(self):
        return self.name

    objects = models.Manager()

    class Meta:
        verbose_name = 'группа статьи доходов'
        verbose_name_plural = 'группы статьи доходов'


class IncomeItem(models.Model):
    name = models.CharField(max_length=300,
                            verbose_name='Нименование')

    group = models.ForeignKey(IncomeItemGroup,
                              on_delete=models.CASCADE,
                              verbose_name='Группа')

    created = models.DateTimeField(default=timezone.now, verbose_name='Создано')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Обновлено')

    def __str__(self):
        return self.name

    objects = models.Manager()

    class Meta:
        verbose_name = 'статья доходов'
        verbose_name_plural = 'статьи доходов'


class Income(models.Model):
    event_date = models.DateTimeField(default=timezone.now,
                                      verbose_name='Дата')

    item = models.ForeignKey(IncomeItem,
                             on_delete=models.CASCADE,
                             blank=True,
                             null=True,
                             verbose_name='Статья доходов')

    contractor = models.ForeignKey('contractors.Contractor',
                                   on_delete=models.CASCADE,
                                   verbose_name='Контрагент')

    product = models.ForeignKey('products.Product',
                                on_delete=models.CASCADE,
                                verbose_name='Продукт')

    product_number = models.IntegerField(default=1,
                                         blank=True,
                                         null=True,
                                         verbose_name='Количество протуктов')

    product_price = models.FloatField(default=0,
                                      blank=True,
                                      null=True,
                                      verbose_name='Стоимость за единицу')

    total_sum = models.FloatField(default=0,
                                  blank=True,
                                  null=True,
                                  verbose_name='Общая стоимость')

    comment = models.TextField(verbose_name='Комментарий',
                               max_length=1000,
                               blank=True,
                               null=True)

    created = models.DateTimeField(default=timezone.now, verbose_name='Создано')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Обновлено')

    objects = models.Manager()

    class Meta:
        verbose_name = 'запись доходов'
        verbose_name_plural = 'записи доходов'

    def __str__(self):
        return '{} ({})'.format(self.event_date, self.product.name)

    def save(self, *args, **kwargs):
        if self.product_price == 0.0:
            self.product_price = self.product.price
        if self.total_sum == 0.0:
            self.total_sum = self.product_number * self.product.price
        super(Income, self).save(*args, **kwargs)
