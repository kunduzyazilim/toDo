"""toDo URL Configuration

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
from .views import toDo_List, userLogin, task_sil

urlpatterns = [
    path(r'', userLogin),
    path(r'tasks/', toDo_List),
    path(r'tasks/delete/(?<pk>[0-9]+)/$', task_sil, name="tDelete"),
    path(r'admin/', admin.site.urls),
]
