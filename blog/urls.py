from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import BlogView

urlpatterns = [
    path('', BlogView.as_view())
]
