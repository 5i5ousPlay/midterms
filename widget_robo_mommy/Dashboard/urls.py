from django.urls import path
from .views import Dashboard_list_view

urlpatterns = [
    path('', Dashboard_list_view, name='Dashboard_list_view'),
]

app_name = "Dashboard"