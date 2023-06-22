from django import forms
from django.contrib.auth.forms import (AuthenticationForm, 
                                       UserCreationForm,
                                       PasswordChangeForm)
from django.contrib.auth.models import User
from user_profile.models import UserProfile
from django.contrib.auth.password_validation import validate_password


class UserAuthenticationForm(AuthenticationForm):
    """Form for user authentication"""
    next_url = forms.CharField(widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        super(UserAuthenticationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegistrationForm(UserCreationForm):
    """Form for user registration"""

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserForm(forms.ModelForm):
    """Form for updating user information"""

    class Meta:
        model = User
        fields = ['first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserProfileForm(forms.ModelForm):
    """Form for updating user profile information"""

    class Meta:
        model = UserProfile
        fields = ['mobile', 'address']
    
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class PasswordUpdateForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_new_password1(self):
        password1 = self.cleaned_data.get('new_password1')
        validate_password(password1, self.user)
        return password1

