from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^store$', views.store, name='store'),
    url(r'^', views.check_db, name='check_db')
]