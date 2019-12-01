from rest_framework import serializers
from .models import Post, PostTag
from user.models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class TagSerializer(serializers.Serializer):
    name = serializers.CharField()
    color = serializers.CharField()


class PostTagSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    tag = TagSerializer()


class UserSerializer(serializers.Serializer):
    profile = UserProfileSerializer()


class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    author = UserSerializer()
    title = serializers.CharField()
    content = serializers.CharField()
    tags = PostTagSerializer(read_only=True, many=True)
