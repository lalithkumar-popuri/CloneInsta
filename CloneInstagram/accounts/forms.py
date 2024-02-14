from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name','username','email','password1','password2']
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "User name"
        self.fields['email'].label = "Email address"