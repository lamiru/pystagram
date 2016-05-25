from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from accounts.forms import SignupForm, UserProfileForm
from accounts.models import UserProfile

User = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully registered!')
            next_url = request.GET.get('next', 'blog:index')
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'form.html', {
        'form': form,
    })

@login_required
def profile_detail(request):
    profile, is_created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile_detail.html', {
        'profile': profile,
    })

@login_required
def profile_edit(request):
    profile, is_created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile information is updated.')
            next_url = request.GET.get('next', 'accounts.views.profile_detail')
            return redirect(next_url)
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'form.html', {
        'form': form,
    })

@login_required
def user_follow(request, username):
    to_user = get_object_or_404(User, username=username)
    is_follow = request.user.is_follow(to_user)

    if request.method == 'POST':
        if not is_follow:
            request.user.follow(to_user)
            messages.success(request, 'You followed {}.'.format(to_user))
        else:
            messages.warning(request, 'You are already following {}.'.format(to_user))
        next_url = request.GET.get('next', '/')
        return redirect(next_url)

    return render(request, 'confirm_form.html', {
        'form_legend': 'Follow {}'.format(to_user),
        'form_desc': 'Do you want to follow {}?'.format(to_user),
        'submit_label': 'Follow',
    })

@login_required
def user_unfollow(request, username):
    to_user = get_object_or_404(User, username=username)
    is_follow = request.user.is_follow(to_user)

    if request.method == 'POST':
        if is_follow:
            request.user.unfollow(to_user)
            messages.success(request, 'You unfollowed {}.'.format(to_user))
        else:
            messages.warning(request, 'You are not following {}.'.format(to_user))

        next_url = request.GET.get('next', '/')
        return redirect(next_url)

    return render(request, 'confirm_form.html', {
        'form_legend': 'Unfollow {}'.format(to_user),
        'form_desc': 'Do you want to unfollow {}?'.format(to_user),
        'submit_label': 'Unfollow',
    })
