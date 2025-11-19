"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('todo/', include('todo.urls'))
"""
from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path,include
from todo import views, cb_views
from user import views as member_views



urlpatterns = [
    path('admin/', admin.site.urls),

    #CBV
    path('', include('todo.urls')),
    #FBV
    path('fb/', include('todo.fbv_urls')),

    #### auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', member_views.signup, name='signup'),
    path('login/', member_views.login, name='login'),
]
