from django.conf.urls import url
 
from app import views
 
app_name = 'vehicle'
 
urlpatterns = [
 
        url(r'^$', views.vehiclelist, name='index'),
        url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='detail'),
        
]