from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Post
from django.db.models import Count
from django.db.models import F
from .serializers import PostSerializer, TagSerializer, Tag, PostTag, PostTagSerializer, CustomSerializer
# Create your views here.


class BlogView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.prefetch_related('tags').all()


class TagListView(ListAPIView):
    serializer_class = CustomSerializer
    queryset = PostTag.objects.values('tag__name').annotate(
        count=Count('tag__name'), id=F('tag__id'), name=F('tag__name'), color=F('tag__color')).order_by('tag__name')
