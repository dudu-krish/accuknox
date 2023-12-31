# Generated by Django 4.2.3 on 2023-08-01 17:01

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_follower_added', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('follows', models.ManyToManyField(blank=True, null=True, related_name='followed_by', to='users.friendslist')),
                ('pending_follow_requests', models.ManyToManyField(blank=True, null=True, related_name='pending_follow_request', to='users.friendslist')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
