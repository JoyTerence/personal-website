from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='personalindex'),
    url(r'^home/$', views.index, name='personalindex'),
    url(r'^links/$', views.links, name='personallinks'),
]
