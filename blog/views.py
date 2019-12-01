from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Post
from .serializers import BlogSerializer
# Create your views here.


class BlogView(ListAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        return Post.objects.prefetch_related('tags').all()
