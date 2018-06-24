from django.views.generic.list import ListView


from . import models


class ExpenseListView(ListView):
    model = models.Expense
    template_name = 'expenses/expenses_list.html'
    context_object_name = 'expenses'


    def get_context_data(self, **kwargs):
        context = super(ExpenseListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        expenses = models.Expense.objects.all()
        expenses_list = []
        for expense in expenses:
            expenses_list.append({
                'contractor': expense.contractor,
                'item': expense.item,
                'frequency_type': expense.frequency_type,
                'products': [product for product in expense.products.all()],
                'products_total_price': expense.products_total_price,
                'products_number_in_pack': expense.products_number_in_pack,
                'products_weight_in_pack': expense.products_weight_in_pack,
                'products_count_in_pack': expense.products_count_in_pack,
                'updated': expense.updated.isoformat()
            })
        return expenses_list