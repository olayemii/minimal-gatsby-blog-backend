from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Post
from .serializers import PostSerializer
# Create your views here.


class BlogView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.prefetch_related('tags').all()
