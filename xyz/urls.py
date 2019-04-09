from django.conf.urls import  url
from . import  views
urlpatterns = [

    url(r'insert',views.insert,name='insert'),



]