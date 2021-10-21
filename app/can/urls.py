from django.urls import path, include
from rest_framework.routers import DefaultRouter

from can import views


router = DefaultRouter()
router.register('can', views.CanViewSet)

app_name = 'can'

urlpatterns = [
    path('', include(router.urls))
]
