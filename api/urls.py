from django.urls import path
from . import views

urlpatterns = [
    path('cans', views.CanItemViews.as_view()),
    path('cans/<int:pk>', views.CanItemViews.as_view())
    ]
