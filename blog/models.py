from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField
from django.template.defaultfilters import slugify
from django.utils.html import strip_tags
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = MDTextField()
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=500, blank=True)
    excerpt = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.excerpt = strip_tags(self.content)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        ordering = ("-created_at",)


class Tag(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=10, default="#000000")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ("-created_at",)


class PostTag(models.Model):
    post = models.ForeignKey(Post, related_name="tags", on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.post.title} - {self.tag.name}"

    class Meta:
        ordering = ("-created_at",)

