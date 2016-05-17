from django.shortcuts import render
from photos.models import Post

def index(request):
    post_list = Post.objects.all()
    return render(request, 'photos/index.html', {
        'post_list': post_list,
    })
