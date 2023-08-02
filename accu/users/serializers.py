from django.contrib.auth.models import User
from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "first_name", "last_name", "email"]


class FriendListSerializer(serializers.ModelSerializer):
  class Meta:
    model = FriendMap
    fields = ["user", "followers", "friend_status", "friend_status_added", "friend_status_updated"]


class MetaFriendSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserFriendMapMeta
    fields = ["user","intermediate_friend_count", "total_friend_count", "cycle"]
