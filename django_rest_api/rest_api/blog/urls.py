from django.urls import path
from .views import UserDetailAPI,RegisterUserAPIView,ChangePasswordView
urlpatterns = [
  path('', RegisterUserAPIView.as_view()),
  path("get-details",UserDetailAPI.as_view()),
  path('change-password', ChangePasswordView.as_view(), name='change-password')
]