from django.conf.urls import url

from . import views
app_name = 'stats'


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index')
]
