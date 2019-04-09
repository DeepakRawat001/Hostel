from django.conf.urls import  url
from . import  views
urlpatterns = [
    url(r'login', views.login , name='login'),
    url(r'signup',views.signup,name='signup'),
    url(r'logout', views.logout, name='logout'),
    url(r'search', views.search, name='search'),
    url(r'result1', views.result1, name='result1'),
    url(r'notice', views.notice,name='notice'),
    url(r'detail', views.detail, name='detail'),
    url(r'room',views.room,name='room'),
    url(r'complain',views.complain,name='complain'),
    url(r'hello',views.hello,name='hello'),
    url(r'seat',views.seat,name='seat'),
    url(r'check',views.check,name='check'),
    url('add',views.add,name="add"),
    url('contact',views.contact,name='contact'),
    url(r'', views.home, name='home'),





]