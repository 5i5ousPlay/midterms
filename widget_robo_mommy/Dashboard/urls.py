from django.urls import path
from .views import (Dashboard_list_view, WidgetUserDetailView,
                    WidgetUserAddView, WidgetUserUpdateView)

urlpatterns = [
    path('dashboard/', Dashboard_list_view, name='Dashboard_list_view'),
    path('widgetusers', WidgetUserDetailView.as_view(),
         name='widgetuser-detail'),
    path('widgetusers', WidgetUserAddView.as_view(),
         name='widgetuser-add'),
    path('widgetusers/<int:pk>/edit/', WidgetUserUpdateView.as_view(),
         name='widgetuser-edit')
]

app_name = "Dashboard"
