from django.contrib import admin
from blog.models import Category, Post, Comment, Tag

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'category', 'title')

admin.site.register(Post, PostAdmin)
