"""
URL configuration for main_app project.

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('birds/', views.bird_index, name='bird-index'),
    path('birds/<int:bird_id>/', views.bird_detail, name='bird-detail'),
    path('birds/create/', views.BirdCreate.as_view(), name='bird-create'),
    path('birds/<int:pk>/update/', views.BirdUpdate.as_view(), name='bird-update'),
    path('birds/<int:pk>/delete/', views.BirdDelete.as_view(), name='bird-delete'),

]

