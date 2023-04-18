"""gamdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from movies.views import homepage
from movies.views import movies
from movies.views import director
from movies.views import actor
from movies.views import movies_detail
from movies.views import director_detail
from movies.views import actor_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('filmy/', movies, name='movies'),
    path('reziseri/', director, name='director'),
    path('herci/', actor, name='actor'),
    path('filmy/<int:id>/', movies_detail, name='movies_detail'),
    path('reziseri/<int:id>/', director_detail, name='director_detail'),
    path('herci/<int:id>/', actor_detail, name='actor_detail'),
]
