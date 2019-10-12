from django.contrib import admin
from django.urls import path
from .Apps.gestiondeusuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('resultado', views.funcion),
]
