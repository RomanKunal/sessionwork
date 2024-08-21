from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set/', views.index),
    path('get/', views.get),
    path('clear/', views.clear),
    path('flush/', views.flush),
]
