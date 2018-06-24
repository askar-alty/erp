from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.IncomeItemGroup)
admin.site.register(models.IncomeItem)
admin.site.register(models.Income)