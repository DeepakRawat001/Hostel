from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from  django.conf import settings
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^homepage/',include('homepage1.urls')),
    url(r'',include('account.urls')),
    url(r'abc',include('xyz.urls')),
]#+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

'''for uploading the media files'''
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

#urlpatterns +=staticfiles_urlpatterns()
#urlpatterns += static(setting.MEDIA_URL.document_root=settings.MEDIA_ROOT)