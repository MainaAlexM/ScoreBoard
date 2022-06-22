from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Project


class Registration(UserCreationForm):
    email = forms.EmailField(
        required=True, widget=forms.EmailInput(attrs={'class': 'my-3 input-val bg-transparent'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(Registration, self).__init__(*args, **kwargs)
        self.fields['password2'].widget.attrs['class'] = 'my-3 input-val bg-transparent'
        self.fields['username'].widget.attrs['class'] = 'input-val bg-transparent'
        self.fields['password1'].widget.attrs['class'] = 'input-val bg-transparent'

    def save(self, commit=True):
        user = super(Registration, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(forms.ModelForm):

    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput())
    # required_css_class = 'required d-none'
    username.widget.attrs.update(
        {'class': 'form-control input-val bg-transparent my-3' })
    password.widget.attrs.update(
        {'class': 'form-control  input-val bg-transparent my-3'})

    class Meta:
        model = Profile
        fields = ('username', 'password')

class SubmitForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title', 'description', 'site_url', 'landing_page')

    def __init__(self, *args, **kwargs):
        super(SubmitForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = ' input-val m-2 form-control'
        self.fields['description'].widget.attrs.update({'class': 'input-val m-2 form-control','rows':'5'})
        self.fields['site_url'].widget.attrs['class'] = 'input-val m-2 form-control'
        self.fields['landing_page'].widget.attrs['class'] = 'input-val m-2 form-control'

class ProfileEditForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    bio = forms.CharField(max_length=50,widget=forms.Textarea)
    profile_image = forms.ImageField()
    
    class Meta:
        model = Profile
        fields = ('username', 'profile_image', 'bio','email')
    username.widget.attrs.update(
        {'class': 'form-control m-2  input-val', 'placeholder': 'Username'})
    email.widget.attrs.update(
        {'class': 'form-control m-2  input-val', 'placeholder': 'Email Address'})
    profile_image.widget.attrs.update(
        {'class': 'form-control m-2  input-val', 'placeholder': 'Profile Picture'})
    bio.widget.attrs.update(
        {'class': 'form-control m-2  input-val', 'placeholder': 'User bio','rows':3, 'cols':35})
