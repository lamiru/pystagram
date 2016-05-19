from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from blog.decorators import owner_required
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'

    def get_context_data(self):
        context = super(PostListView, self).get_context_data()
        context['count'] = self.request.session.get('index_page_count', 0) + 1
        self.request.session['index_page_count'] = context['count']
        context['lorempixel_categories'] = (
            'abstract', 'animals', 'business', 'cats', 'city', 'food', 'night',
            'life', 'fashion', 'people', 'nature', 'sports', 'technics', 'transport',
        )
        return context

index = PostListView.as_view()

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get_object(self, *args, **kwargs):
        if 'uuid' in self.kwargs:
            return get_object_or_404(Post, uuid=self.kwargs['uuid'])
        return super(PostDetailView, self).get_object(*args, **kwargs)

detail = PostDetailView.as_view()

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.ip = self.request.META['REMOTE_ADDR']
        return super(PostCreateView, self).form_valid(form)

new = login_required(PostCreateView.as_view())

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'form.html'

    @method_decorator(login_required)
    @method_decorator(owner_required(Post, 'pk'))
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)

edit = PostUpdateView.as_view()

@login_required
def comment_new(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = get_object_or_404(Post, pk=pk)
            comment.save()
            messages.success(request, 'Saved the comment.')
            return redirect(comment.post)
    else:
        form = CommentForm()
    return render(request, 'form.html', {
        'form': form,
    })

@login_required
@owner_required(Comment, 'pk')
def comment_edit(request, post_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, pk=pk)
            comment.save()
            messages.success(request, 'Edited the comment.')
            return redirect(comment.post)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'form.html', {
        'form': form,
    })

@login_required
@owner_required(Comment, 'pk')
def comment_delete(request, post_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Deleted the comment.')
        return redirect(comment.post)
    return render(request, 'blog/comment_delete_confirm.html', {
        'comment': comment,
    })
