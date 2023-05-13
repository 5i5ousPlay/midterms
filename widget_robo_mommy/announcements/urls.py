from django.urls import path
from .views import index, AnnouncementDetailView, AnnouncementAddView, AnnouncementEditView

urlpatterns = [
    path('announcements/', index, name='index'),
    path('announcements/<int:pk>/details/', AnnouncementDetailView.as_view(), name='announcement-detail'),
    path('announcements/add/', AnnouncementAddView.as_view(), name='announcement-add'),
    path('announcements/<int:pk>/edit/', AnnouncementEditView.as_view(), name='announcement-edit'),
]

app_name = "announcements"