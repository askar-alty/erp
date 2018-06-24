from django.views.generic import ListView

# Create your views here.
from . import models


class IncomeListView(ListView):
    model = models.Income
    template_name = 'incomes/incomes_list.html'
    context_object_name = 'incomes'

    def get_context_data(self, **kwargs):
        context = super(IncomeListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        incomes = models.Income.objects.all()
        incomes_list = []
        for income in incomes:
            incomes_list.append({
                'date': '{}-{}-{}'.format(income.event_date.day, income.event_date.month, income.event_date.day),
                'contractor': income.contractor,
                'item': income.item,
                'product': income.product,
                'product_number': income.product_number,
                'product_price': income.product_price,
                'total_sum': income.total_sum,
                'created': income.created.isoformat(),
                'updated': income.updated.isoformat()
            })
        return incomes_list