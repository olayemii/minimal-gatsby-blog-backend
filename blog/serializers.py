from rest_framework import serializers
from .models import Post, PostTag, Tag
from user.models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class PostTagSerializer(serializers.ModelSerializer):
    tag = TagSerializer()

    class Meta:
        model = PostTag
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        exclude = ("password", "is_superuser", "is_staff",
                   "user_permissions", "groups", "last_login",)


class PostSerializer(serializers.ModelSerializer):
    tags = PostTagSerializer(read_only=True, many=True)
    author = UserSerializer()

    class Meta:
        model = Post
        fields = "__all__"
