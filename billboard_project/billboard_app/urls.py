from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^comment$', views.comment, name='comment'),
    url(r'^store$', views.store, name='store'),
    url(r'^$', views.check_db, name='check_db')
]