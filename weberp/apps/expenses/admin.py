from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.ExpenseItemGroup)
admin.site.register(models.ExpenseItem)
admin.site.register(models.Expense, models.ExpenseAdmin)
