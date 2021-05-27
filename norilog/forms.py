from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", 'email', "password1", "password2")

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class LoginForm(AuthenticationForm):
    def __init__(self, request: Any, *args: Any, **kwargs: Any) -> None:
        super().__init__(request=request, *args, **kwargs)


