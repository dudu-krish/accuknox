from django.urls import path

from .views import RegisterUserAPIView, LoginAPIView

urlpatterns = [
  path('signup',RegisterUserAPIView.as_view()),
  path('login', LoginAPIView.as_view()),
]
