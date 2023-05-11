from django.urls import path
from .views import (
    index, AssignmentDetailsView,
    AddAssignmentView, EditAssignmentView
)

urlpatterns = [
    path('', index, name='index'),
    path('add/', AddAssignmentView.as_view(), name='assignments=add'),
    path('<int:pk>/edit/', EditAssignmentView.as_view(), name='assignments-edit'),
    path('<int:pk>/details/', AssignmentDetailsView.as_view(), name='assignments-item'),
]

app_name = "assignments"
