from django.conf.urls import url
from . import views
app_name = 'incomes'

urlpatterns = [
    url(r'^$', views.IncomeListView.as_view(), name='incomes_list')
]