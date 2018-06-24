from django.db import models
from django.utils import timezone


# Create your models here.


class Contractor(models.Model):
    TYPES = (
        ('individual_entrepreneur', 'Инидивидуальный предприниматель'),
        ('legal_entity', 'Юридическое лицо')
    )

    TAXATION_FORMS = (
        ('traditional', 'Традиционная (общая) система (режим) налогообложения'),
        ('simplified', 'Упрощённая система налогообложения '),
        ('single_tax_on_imputed_income', 'Единый налог на вменённый доход'),
        ('unified_agricultural', 'Единый сельскохозяйственный налог'),
        ('patent', 'Патентная система налогообложения')
    )

    name = models.CharField(max_length=300,
                            verbose_name='Наименование')

    type = models.CharField(max_length=100,
                            choices=TYPES,
                            verbose_name='Вид')

    taxation_form = models.CharField(max_length=350,
                                     choices=TAXATION_FORMS,
                                     verbose_name='Форма налогооблажения')

    provider = models.BooleanField(default=False,
                                   verbose_name='Поставщик?')

    client = models.BooleanField(default=False,
                                 verbose_name='Клиент?')

    created = models.DateTimeField(default=timezone.now, verbose_name='Создано')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Обновлено')

    def __str__(self):
        return self.name

    objects = models.Manager()

    class Meta:
        verbose_name = 'конрагент'
        verbose_name_plural = 'конрагенты'
