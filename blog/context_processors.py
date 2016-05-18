from blog.models import Post

def summary(request):
    post_count = Post.objects.all().count()
    return {
        'post_count': post_count,
    }
