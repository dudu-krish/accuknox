# Generated by Django 4.2.3 on 2023-08-02 08:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_alter_friendmap_followers_alter_friendmap_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendmap',
            name='first_friend_added_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='friendmap',
            name='friend_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='friendmap',
            name='friend_status_added',
            field=models.DateTimeField(blank=True, null=True, verbose_name='modificationtime'),
        ),
        migrations.CreateModel(
            name='UserFriendMapMeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intermediate_friend_count', models.IntegerField(blank=True, null=True)),
                ('total_friend_count', models.IntegerField(blank=True, null=True)),
                ('cycle', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]