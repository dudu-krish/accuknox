from django.urls import path

from .views import *

urlpatterns = [
  path("get-details",UserDetailAPI.as_view()),
  path("get-followers", FriendListAPI.as_view()),
  path("send-friend-request", SendFriendRequest.as_view()),
  path("change-friend-status/<int:pk>", ChangeFriendRequestStatusAPI.as_view()),
]
