from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from django.views.generic.base import RedirectView
from . import views
urlpatterns = [
    #用户登录 退出 注册

    path('login/', views.index),
    path('user_login/',views.user_login),
    path('user_logoutAction/',views.user_logoutAction),
    # path('login',views.login),
    # path('admin/',admin.site.urls)
]