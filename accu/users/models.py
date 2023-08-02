# Create your models here.
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserFriendMapMeta(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    intermediate_friend_count = models.IntegerField(blank=True, null=True)
    total_friend_count = models.IntegerField(blank=True, null=True)
    cycle = models.DateTimeField(blank=True, null=True)


class FriendMap(models.Model):
    class FriendStatus(models.IntegerChoices):
        ACCEPTED = 0
        REJECTED = 1
        PENDING = 2
        CONFUSED = 3
        BLOCKED = 4
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    followers = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="friend_followers")
    friend_status = models.IntegerField(choices=FriendStatus.choices)
    friend_status_added = models.DateTimeField(verbose_name="modificationtime", blank=True, null=True)
    friend_status_updated = models.DateTimeField(blank=True, null=True)
    friend_count = models.IntegerField(blank=True, null=True)
    first_friend_added_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.email} sent friend request to {self.followers.email}"


@receiver(post_save, sender=FriendMap)
def enter_friend_map(sender, instance, **kwargs):
    friend_map_instance, created = UserFriendMapMeta.objects.get_or_create(user=instance.user,
                                                                           defaults={
                                                                               "intermediate_friend_count": 1,
                                                                               "total_friend_count": 1,
                                                                               "cycle": datetime.now(),
                                                                           })
    if not created:
        friend_count = friend_map_instance.intermediate_friend_count
        if friend_count == 3:
            friend_map_instance.intermediate_friend_count = 1
            friend_map_instance.cycle = datetime.now()
        else:
            friend_map_instance.intermediate_friend_count = friend_map_instance.intermediate_friend_count + 1
        friend_map_instance.total_friend_count = friend_map_instance.total_friend_count + 1
        friend_map_instance.save()

