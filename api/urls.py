from django.urls import path
from api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
