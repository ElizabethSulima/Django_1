"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from .views import catalog, show_product, index, phone_detail_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('catalog/', catalog, name='catalog'),
    path('catalog/<slug:slug>/', show_product, name='phone'),
    path('catalog/<slug:slug>/', phone_detail_view, name='phone_detail'),
]