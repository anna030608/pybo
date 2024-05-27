from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import UserForm


def logout_view(request):
    logout(request)
    return redirect('index')


def signup(request):
    """
    계정생성
    """
    # user의 생성을 담당..
    # POST : 내가 입력한 user내용들을 DB에 저장해줘라..
    if request.method == "POST":
        form = UserForm(request.POST)   # 가져와서 폼에 저장..
        if form.is_valid():
            form.save()    # 저장..
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # authenticate : 회원 인증. DB에 해당 username, password가 저장되어 있는지 확인.
            #               -> 저장되어 있다면 인증 완료! -> 권한 부여할 수 있게 됨.

            login(request, user)
            # 권한을 주는 것. (admin 까진 아님.)
            # 어느 권한을 줄 수 있는지를 판별. 후 권한 부여.
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
    # 이때의 form 은 4개의 필드가 있다.
    # 1.user-name 2.password 3.password 확인 4.e-mail