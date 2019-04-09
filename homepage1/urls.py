from django.conf.urls import  url
from . import  views
urlpatterns = [
    url(r'index/',views.index,name='index'),

    #url(r'^[0-9]/$',views.detail),
    url(r'^(?P<movie_id>[0-9]+)/$',views.detail,name='detail'),
    #for favourite song

    #url(r'^(?P<movie_id>[0-9]+)/favourite/$',views.favourite,name="favourite"),
    url(r'form/', views.count ,name='count'),
]
