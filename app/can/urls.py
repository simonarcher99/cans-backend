from django.urls import path

from can import views


app_name = 'can'

urlpatterns = [
    path('', views.CanViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='can')
]
