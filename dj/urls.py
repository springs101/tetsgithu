"""dj URL Configuration

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
from django.conf.urls import include,url
from syn_edb import views as syn_edb_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^syn/getdata', syn_edb_views.getData),
    url(r'^syn/getData_remedy', syn_edb_views.getData_remedy),
    url(r'^syn/hart_beat', syn_edb_views.hartbeat),
    url(r'^syn/bak_GetDataLog', syn_edb_views.bakGetDataLog),
]
