from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# user 를 생성할때 필요한 폼 : UserCreationForm
class UserForm(UserCreationForm):
    # user model에서 이메일을 사용하겠다..
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "email")