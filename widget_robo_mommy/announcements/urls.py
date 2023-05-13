from django.urls import path
from .views import index

urlpatterns = [
    path('announcements/', index, name='index'),
    path('announcements/<int:pk>/details/', AnnouncementDetailView.as_view(), name='announcement-detail'),
    path('announcements/add/', AnnouncementDetailView.as_view(), name='announcement-add'),
    path('announcements/<int:pk>/edit/', AnnouncementDetailView.as_view(), name='announcement-edit'),
]

app_name = "announcements"