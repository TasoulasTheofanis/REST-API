from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views #from api folder import views.py file

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
