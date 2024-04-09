from django.contrib import admin
from django.urls import path, include
from portfolio import views as portfolio_views
from contact import views as contact_views
from django.conf import settings

urlpatterns = [
    path('portfolio/', portfolio_views.portfolio, name="portfolio"),
]