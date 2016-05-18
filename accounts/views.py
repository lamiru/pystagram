from django.shortcuts import render

def profile_detail(request):
    return render(request, 'accounts/profile_detail.html', {
    })
