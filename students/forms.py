from typing import Any
from django import forms
from courses.models import Course
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.HiddenInput)

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'required': '',
            'name': 'username',
            'id': 'username',
            'type': 'text',
            'class': 'border border-blue-950 w-[390px] h-16 text-2xl caret-blue-950',
            'placeholder': 'Lustrous Dromio',
        })
        self.fields['password1'].widget.attrs.update({
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'class': 'border border-blue-950 w-[390px] h-16 text-2xl caret-blue-950',
        })
        self.fields['password2'].widget.attrs.update({
            'required': '',
            'name': 'password2',
            'id': 'password2',
            'type': 'password',
            'class': 'border border-blue-950 w-[390px] h-16 text-2xl caret-blue-950',
        })

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']