from django.forms import ModelForm
from .models import Assignment
from django import forms


class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = "__all__"

        labels = {
            'name': '',
            'description': '',
            'course': 'Course: ',
            'perfect_score': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Assignment Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'course': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Course'}),
            'perfect_score': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Perfect Score'}),
            'passing_score': forms.HiddenInput(),
        }