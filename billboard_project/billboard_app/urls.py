from django.conf.urls import url
from . import views
from django.contrib.auth import views as authviews

urlpatterns = [
    url(r'^comment$', views.comment, name='comment'),
    url(r'^store$', views.store, name='store'),
    url(r'^$', views.check_db, name='check_db'),
    url(r'login/$', authviews.login, name='login'),
    url(r'^logout/$', authviews.logout, {'next_page': '/'},name='logout')
]