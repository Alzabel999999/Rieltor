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
from django.urls import path, include
from second import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<int:id>/', views.single, name='single'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('?page=<int:id>/', views.index, name='index1'),
    path('url_replace', views.url_replace, name='url_replace'),
    path('saveform', views.saveform, name='saveform'),
    path('about', views.about, name='about')
]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)