from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('slut/', views.slut, name = 'slut'),
]
