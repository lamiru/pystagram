from django.shortcuts import render, redirect
from accounts.forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            next_url = request.GET.get('next', 'blog.views.index')
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'form.html', {
        'form': form,
    })

def profile_detail(request):
    return render(request, 'accounts/profile_detail.html', {
    })
