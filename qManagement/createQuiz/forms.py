from django.forms import ModelForm
from .models import *
from django import forms


class ClassListForm(ModelForm):
    className = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    subject = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    section = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ), )
    enrollKey = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),)

    class Meta:
        model = ClassList
        fields = ['className', 'subject', 'section', 'enrollKey']


class AddTopic(ModelForm):
    topic = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    description = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    class Meta:
        model = TopicList
        fields = ['topic', 'description']


class AddQuiz(ModelForm):
    quiz = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    description = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    class Meta:
        model = QuizList
        fields = ['quiz', 'description']


class AddQuestion(ModelForm):
    question = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    description = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    cA = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    cB = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    cC = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    cD = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'sample'
            }
        ),
    )
    answer = forms.Select(
        choices=[
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('D', 'D'),
        ],
    )

    class Meta:
        model = QuestionSet
        fields = ['question', 'description', 'cA', 'cB', 'cC', 'cD', 'answer']
