from django import forms
from django.contrib.auth.models import User
from apps.user.models import UserProfileInfo


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
        widgets = {
            # telling Django your password field in the mode is a password input on the template
      		'first_name': forms.TextInput(attrs={'placeholder': 'Name'}),
         	'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
         	'username': forms.TextInput(attrs={'placeholder': 'Nickname'}),
           	'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),            
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail'}),         	
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('age', 'number_phone', 'github')
        widgets = {
            'age': forms.NumberInput(attrs={'placeholder': 'Age', 'min': 18}),
            'number_phone': forms.NumberInput(attrs={'placeholder': 'Phone'}),
           	'github': forms.URLInput(attrs={'placeholder': 'Github'})
        }
