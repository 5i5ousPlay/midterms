from django.forms import ModelForm
from .models import Course, Assignment


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = "__all__"


class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = "__all__"
