# Generated by Django 2.2.7 on 2019-12-16 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light_gallery_video', '0002_lightgalleryvideo_muted'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='muted',
            field=models.BooleanField(default=True),
        ),
    ]
