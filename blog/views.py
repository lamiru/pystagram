from django.http import Http404
from django.shortcuts import render, get_object_or_404
from blog.models import Post

def index(request):
    count = request.session.get('index_page_count', 0) + 1
    request.session['index_page_count'] = count

    post_list = Post.objects.all()

    lorempixel_categories = (
        'abstract', 'animals', 'business', 'cats', 'city', 'food', 'night',
        'life', 'fashion', 'people', 'nature', 'sports', 'technics', 'transport',
    )

    return render(request, 'blog/index.html', {
        'count': count,
        'post_list': post_list,
        'lorempixel_categories': lorempixel_categories,
    })

def detail(request, pk=None, uuid=None):
    if pk:
        post = get_object_or_404(Post, pk=pk)
    elif uuid:
        post = get_object_or_404(Post, uuid=uuid)
    else:
        raise Http404

    return render(request, 'blog/detail.html', {
        'post': post,
    })
