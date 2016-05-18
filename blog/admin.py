from django.contrib import admin
from blog.models import Category, Post, Comment, Tag

admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuid', 'category', 'title', 'author')
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'content')
    search_fields = ('content',)

admin.site.register(Comment, CommentAdmin)
