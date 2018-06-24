from django.conf.urls import url
from . import views
app_name = 'expenses'

urlpatterns = [
    url(r'^$', views.ExpenseListView.as_view(), name='expenses_list')
]