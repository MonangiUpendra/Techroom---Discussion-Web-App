from django.forms import ModelForm
from .models import Room, User  # Import your custom User model
from django.contrib.auth.hashers import make_password
from django import forms
from django.contrib.auth.hashers import check_password, make_password
from .models import User



class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['topic', 'name', 'description']  # Exclude fields that should be set automatically
        exclude=['host','participants']

from django import forms
from django.contrib.auth.hashers import make_password
from .models import User  # Import your custom User model

class CustomRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, label="Username")  # ✅ Add username field
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password", required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])  # ✅ Hash password before saving

        

        
        if commit:
            user.save()
        return user



class UpdateUserForm(forms.ModelForm):
    new_password = forms.CharField(widget=forms.PasswordInput, required=False, label="New Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=False, label="Confirm New Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'bio', 'avatar']

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password or confirm_password:
            if new_password != confirm_password:
                raise forms.ValidationError("New passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        new_password = self.cleaned_data.get("new_password")

        if new_password:
            user.password = make_password(new_password)

        if commit:
            user.save()
        return user

