from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.admin import ModelAdmin


class ExpenseItemGroup(models.Model):
    name = models.CharField(max_length=300,
                            verbose_name='Наименование')

    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    objects = models.Manager()

    class Meta:
        verbose_name = 'группа статей расходов'
        verbose_name_plural = 'группы статей расходов'


class ExpenseItem(models.Model):
    name = models.CharField(max_length=300,
                            verbose_name='Наименование')

    group = models.ForeignKey(ExpenseItemGroup,
                              on_delete=models.CASCADE,
                              verbose_name='Группа')

    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    objects = models.Manager()

    class Meta:
        verbose_name = 'статья расходов'
        verbose_name_plural = 'статьи расходов'


class Expense(models.Model):
    FREQUENCY_TYPE = (('постоянные', 'постоянные'),
                      ('переменные', 'переменные'))

    contractor = models.ForeignKey('contractors.Contractor',
                                   on_delete=models.CASCADE,
                                   verbose_name='Контрагент')

    item = models.ForeignKey(ExpenseItem,
                             on_delete=models.CASCADE,
                             blank=True,
                             null=True,
                             verbose_name='Статья расходов')

    frequency_type = models.CharField(max_length=300,
                                      choices=FREQUENCY_TYPE,
                                      verbose_name='Тип расхода')

    products = models.ManyToManyField('products.Product',
                                      verbose_name='Продукты')

    products_total_price = models.FloatField(default=0,
                                             blank=True,
                                             null=True,
                                             verbose_name='Общая стоимость')

    products_number_in_pack = models.FloatField(default=1,
                                                blank=True,
                                                null=True,
                                                verbose_name='Количество в упаковке')

    products_weight_in_pack = models.FloatField(default=0,
                                                blank=True,
                                                null=True,
                                                verbose_name='Кг в упаковке')

    products_count_in_pack = models.FloatField(default=1,
                                               blank=True,
                                               null=True,
                                               verbose_name='Штук в упаковке')

    comment = models.TextField(verbose_name='Комментарий',
                               max_length=1000,
                               blank=True,
                               null=True)

    created = models.DateTimeField(default=timezone.now, verbose_name='Создано')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Обновлено')

    objects = models.Manager()

    class Meta:
        ordering = ['updated']
        verbose_name = 'запись расходов'
        verbose_name_plural = 'записи расходов'

    def __str__(self):
        return "{} ({})".format(self.updated, ', '.join([product.name for product in self.products.all()]))


class ExpenseAdmin(ModelAdmin):
    class Meta:
        model = Expense

    def save_model(self, request, obj, form, change):
        obj.save()

    def save_related(self, request, form, formsets, change):
        super(ExpenseAdmin, self).save_related(request, form, formsets, change)
        products = form.cleaned_data.get('products')
        if products:
            total_price = 0
            for product in products:
                form.instance.products.add(product)
                total_price += product.price
            if form.instance.products_total_price == 0:
                form.instance.products_total_price = total_price
            form.instance.save()
