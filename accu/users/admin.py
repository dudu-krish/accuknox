from django.contrib import admin

from .models import *


class FriendInLine(admin.ModelAdmin):
    model = FriendMap
    fields = ['email']



admin.site.register(FriendMap)
admin.site.register(UserFriendMapMeta)
