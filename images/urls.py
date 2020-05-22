from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = "home_welcome"),
    url('^saved/$',views.firstImages,name="saved_images")
]