from core import views
from django.urls import path
urlpatterns = [
    path('', views.home, name="home"),
    path('about-me/', views.about, name="about"),
]