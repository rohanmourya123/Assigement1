from django import forms
from .models import Post,user
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User



class form(forms.ModelForm):
    class meta:
        model = Post
        fields =('__all__')


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()

# class signup_form(UserCreationForm):
#     class Meta:
#         model=User
#         fields= ("__all__")


class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )
# class signup_form(UserCreationForm):
#     class Meta:
#         model = user
#         fields = ('first_name', 'last_name', 'username', 'email', 'password',)