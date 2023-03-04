from django.urls import path
from .views import DashboardView


urlpatterns = [
    path('Dashboard/', DashboardView.as_view()),
]

app_name = "Dashboard"