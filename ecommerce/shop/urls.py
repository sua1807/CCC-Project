from django.conf.urls import url
from .import views

urlpatterns = [
#shop
    url(r'^$', views.index, name='index'),
    #shop/product id
    url(r'(?P<Catalog_id>[0-9]+)/$', views.detail, name='detail'),
    
]
#url("^$", views.index),
