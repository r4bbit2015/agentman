from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from django.views.generic.base import RedirectView
from . import views
urlpatterns = [
    # path('', views.login),
    path('login/',views.login),
    # path('admin/',admin.site.urls)
]