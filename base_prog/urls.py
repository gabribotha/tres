# root_app/urls.py

from django.conf.urls import url

from base_prog import views

urlpatterns = [
    url(r'', views.index, name='index'),
]