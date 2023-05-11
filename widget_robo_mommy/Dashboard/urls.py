from django.urls import path
from .views import (Dashboard_list_view, WidgetUserDetailView,
                    WidgetUserAddView, WidgetUserUpdateView)

urlpatterns = [
    path('Dashboard/', Dashboard_list_view, name='Dashboard_list_view'),
    path('Widgetusers/<int:pk>/details', WidgetUserDetailView.as_view(),
         name='widgetuser-detail'),
    path('Widgetusers/add/', WidgetUserAddView.as_view(), 
         name='widgetuser-add'),
    path('Widgetusers/<int:pk>/edit/', WidgetUserUpdateView.as_view(),
         name='widgetuser-edit')
         
]

app_name = "Dashboard"