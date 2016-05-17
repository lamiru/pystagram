from django.contrib import admin
from blog.models import Category, Post, Comment, Tag

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
