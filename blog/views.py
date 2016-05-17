from django.conf import settings
from django.shortcuts import render, get_object_or_404
from blog.models import Post

def index(request):
    count = request.session.get('index_page_count', 0) + 1
    request.session['index_page_count'] = count

    post_list = Post.objects.all()

    return render(request, 'blog/index.html', {
        'count': count,
        'post_list': post_list,
    })

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/detail.html', {
        'post': post,
    })
