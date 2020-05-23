from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = "home_welcome"),
    url('^malawi/$',views.malawi,name="malawi"),
    url('^heaven/$',views.heaven,name="heaven"),
    url('^europe/$',views.malawi,name="europe"),
    url('^mountains/$',views.malawi,name="mountains"),
    url('^africa/$',views.malawi,name="africa"),
    url('^search/$',views.search_results,name="search_results"),
    url('^gallery/$',views.gallery,name="gallery"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)