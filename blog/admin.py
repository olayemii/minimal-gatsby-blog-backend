from django.contrib import admin
from .models import Post, Tag, PostTag
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/english.js',)


admin.site.register(Post, PostAdmin)
admin.site.register((Tag, PostTag))
