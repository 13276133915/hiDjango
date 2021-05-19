"""helloDjango URL Configuration

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
from django.shortcuts import render
from django.urls import path, include
from django.http import HttpRequest, HttpResponse


# 声明views的处理函数
# view处理函数必须要求声明一个request参数，表示客户端的请求对象
# 请求对象中包含那些信息 请求头headers（method， url， path_info, COOKIES）
import xadmin


def index(request: HttpRequest):
    users = [{'id': 1, 'name':'disen'},
            {'id': 2, 'name':'jack'},
            {'id': 3, 'name':'李虎'}]
    # return HttpResponse('<h1>hi.Django</h1>'.encode('utf-8'))
    return render(request, 'index.html', {'user':users,
                               'msg':'所有用户'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('user/',include('mainapp.urls'))
]
