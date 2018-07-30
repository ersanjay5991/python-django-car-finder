"""VehicleFinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from app import views 

from django.contrib.auth.views import (
    login,
    logout,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
)

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('index/', views.index), 
    path('show',views.show),  
    path('import_csv',views.read_csv),  
    url(r'^admin/',admin.site.urls, name='admin'),
    url(r'^$', views.index, name='Home'),
    url(r'about/', views.about, name='aboutsus'),
    #url(r'contact', views.contact, name='contact'),
    url(r'rental/', views.carrent, name='carrent'),

    path('import_csv',views.read_csv),  

    #sqllite db operation
    path('dboperation',views.dboperation),  
    path('booknow',views.book_now),
    path('contactus/',views.contactus),  
    path('viewbuys',views.viewbuys),
   
    
    url(r'^vehicle/', include('app.urls')),

    url(r'^login/$',login,{'template_name': 'accounts/login.html'},name="login"),
    url(r'^logout/$',logout,{'template_name': 'accounts/logout.html'},name="logout"),
    url(r'^register/$',views.register,name='register'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^profile/edit/$',views.edit_profile,name='edit_profile'),
    url(r'^change_password/$',views.change_password,name='change_password'),
    url(r'^password_reset/$', password_reset, name='password_reset'),
    url(r'^password_reset/done/$',password_reset_done,name='password_reset_done'),
    url(r'^password_reset_confirm/$',password_reset_confirm,name='password_reset_confirm'),
    url(r'^password_reset_complete/$',password_reset_complete,name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "VehicleFinder Admin"
admin.site.site_title = "VehicleFinder Admin Portal"
admin.site.index_title = "Welcome to VehicleFindePortal"