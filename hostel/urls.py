from django.conf.urls import  url
from django.contrib import admin
from django.urls import path,include
from  django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^homepage/',include('homepage1.urls')),
    url(r'',include('account.urls')),
    url(r'abc',include('xyz.urls')),
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
