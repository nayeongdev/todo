from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import User

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'accounts/profile.html', {'user': user})
