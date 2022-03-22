from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from common.models import User, UserManager


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = User(request.POST)
        if form.is_valid():
            form.save()
            # first_name = form.cleaned_data.get('first_name')
            # last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증

            login(request, user)  # 로그인
            return redirect(reverse('insta:allPhotoAB'))
    else:
        form = User()

    return render(request, 'common/signup.html', {'form': form})

# def signup(request):
#     pass
