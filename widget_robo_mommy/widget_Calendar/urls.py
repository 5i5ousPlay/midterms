from django.urls import path
from .views import (index, EventDetailView, EventAddView, EventUpdateView)


urlpatterns = [
    path('', index, name='index'),
    path('events/<int:pk>/details/', EventDetailView.as_view(),
         name='event-detail'),
    path('events/add/', EventAddView.as_view(),
         name='event-add'),
    path('events/<int:pk>/edit/', EventUpdateView.as_view(),
         name='event-edit')
]

app_name = "widget_Calendar"
