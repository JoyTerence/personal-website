from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.contact, name='contactemail'),
    url(r'^thankyou/', views.thankyou, name='contactthankyou')
]
