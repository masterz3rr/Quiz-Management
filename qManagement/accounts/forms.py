from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class TeacherForm(ModelForm):
    profile_pic = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'id': 'fileInput',
                'class': 'form-control',
            }
        ),
    )

    firstname = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    lastname = forms.CharField(
        label='Lastname',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    phone = forms.CharField(
        label='Phone',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    user_email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={
                'id': 'emailField',
                'class': 'form-control',
            }
        ),)

    class Meta:
        model = Teacher
        fields = ['firstname', 'lastname', 'user_email', 'phone', 'profile_pic']
        exclude = ['user']


class StudentForm(ModelForm):
    user_email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={
                'id': 'emailField',
                'class': 'form-control',
            }
        ),)

    profile_pic = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'id': 'profile_pic',
                'class': 'form-control',
            }
        ),
    )

    firstname = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    lastname = forms.CharField(
        label='Lastname',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    phone = forms.CharField(
        label='Phone',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'user_email', 'phone', 'profile_pic']
        exclude = ['user']


class CreateTeacherForm(UserCreationForm):
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingInput',
                'placeholder': 'Username'
            }
        ),
    )
    email = forms.EmailField(
        label='Email address',
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingEmail',
                'placeholder': 'Username'
            }
        ),
    )
    password1 = forms.CharField(
        label='Password1',
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingPassword1',
                'placeholder': 'Username'
            }
        ),
    )
    password2 = forms.CharField(
        label='Password2',
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingPassword2',
                'placeholder': 'Username'
            }
        ),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateTeacherForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['id'] = 'floatingInput'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email address'
        self.fields['email'].widget.attrs['id'] = 'floatingInput'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['id'] = 'floatingInput'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Re-enter password'
        self.fields['password2'].widget.attrs['id'] = 'floatingPassword2'


class CreateStudentForm(UserCreationForm):
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingInput',
                'placeholder': 'Username'
            }
        ),
    )
    email = forms.EmailField(
        label='Email address',
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingEmail',
                'placeholder': 'Username'
            }
        ),
    )
    password1 = forms.CharField(
        label='Password1',
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingPassword1',
                'placeholder': 'Username'
            }
        ),
    )
    password2 = forms.CharField(
        label='Password2',
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingPassword2',
                'placeholder': 'Username'
            }
        ),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateStudentForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['id'] = 'floatingInput'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email address'
        self.fields['email'].widget.attrs['id'] = 'floatingInput'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['id'] = 'floatingInput'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Re-enter password'
        self.fields['password2'].widget.attrs['id'] = 'floatingPassword2'
