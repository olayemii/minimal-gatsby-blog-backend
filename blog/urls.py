from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import BlogView, TagListView

urlpatterns = [
    path('list', BlogView.as_view()),
    path('tags', TagListView.as_view())
]
