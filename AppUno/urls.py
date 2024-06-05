from AppUno import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('forms/', views.agregarSituacion),
    # path('forms/update/<int:id>'),
    # path('forms/delete/<int:id>'),
]
