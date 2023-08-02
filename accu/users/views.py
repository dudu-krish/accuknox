from django.contrib.auth.models import User
from rest_framework import filters
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from .models import *
from .serializers import UserSerializer, FriendListSerializer


# Create your views here.
# Class based view to Get User Details using Token Authentication
class UserDetailAPI(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  authentication_classes = (TokenAuthentication,)
  permission_classes = (permissions.IsAuthenticated,)
  filter_backends = [filters.SearchFilter]
  search_fields = ['^email', '^first_name']


class FriendListAPI(generics.ListAPIView):
  serializer_class = FriendListSerializer
  authentication_classes = (TokenAuthentication,)
  permission_classes = (permissions.IsAuthenticated,)

  def get_queryset(self):
    """
    This API can be used to get all the friends logged in by the user.
    The query param friend_status is the accepted, rejected, pending etc.
    :return:
    """
    user = self.request.user
    return FriendMap.objects.filter(user=user, friend_status=self.request.query_params.get("friend_status"))


class SendFriendRequest(generics.CreateAPIView):
  #queryset = FriendMap.objects.all()
  serializer_class = FriendListSerializer
  authentication_classes = (TokenAuthentication,)
  permission_classes = (permissions.IsAuthenticated,)

  def get_queryset(self):
    user = self.request.user
    return FriendMap.objects.filter(user=user)

  def create(self, request, *args, **kwargs):
    """
    This API can be used to send friend request by logged in user. The user cannot send more than 3 friend request
    in 1 minute
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    try:
      request.data['user'] = self.request.user.id
      request.data['friend_status_added'] = datetime.now()

      # User cannot send friend request 3 times in 1 minute
      cycle_obj = UserFriendMapMeta.objects.filter(user=self.request.user).first()
      if cycle_obj:
        intermediate_friend = cycle_obj.intermediate_friend_count
        cycle_date = cycle_obj.cycle
        if intermediate_friend == 3:
          time_delta = cycle_date.replace(tzinfo=datetime.now().tzinfo) - datetime.now()
          print(time_delta.total_seconds())
          if abs(time_delta.total_seconds()) < 60:
            return Response(
              {"message": "You can send only 3 friend request in 1 minute."},
              status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
            )

      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      headers = self.get_success_headers(serializer.data)

      return Response(
        {"message": "Friend request sent"},
        status=status.HTTP_201_CREATED,
        headers=headers,)
    except Exception as e:
      print(e)
      # log it


class ChangeFriendRequestStatusAPI(generics.UpdateAPIView):
  queryset = FriendMap.objects.all()
  serializer_class = FriendListSerializer
  authentication_classes = (TokenAuthentication,)
  permission_classes = (permissions.IsAuthenticated,)

  def update(self, request, *args, **kwargs):
    """
    Friend request status can be changed using this API. The status can be changed to accepted, rejected, pending etc
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    request.data['user'] = self.request.user.id
    request.data['friend_status_updated'] = datetime.now()
    return super(ChangeFriendRequestStatusAPI, self).update(request, *args, **kwargs)

























