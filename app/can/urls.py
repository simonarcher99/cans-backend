from django.urls import path

from can import views


app_name = 'can'

urlpatterns = [
    path('', views.CanViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='can'),
    path('<pk>', views.CanViewSet.as_view(
        {'patch': 'partial_update', 'delete': 'destroy',
            'get': 'retrieve', 'put': 'update'}
    ), name='can')
]
