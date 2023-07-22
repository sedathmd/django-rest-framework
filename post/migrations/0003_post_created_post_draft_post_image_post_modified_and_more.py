# Generated by Django 4.2.2 on 2023-06-15 07:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 15, 7, 25, 50, 332157, tzinfo=datetime.timezone.utc), editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=datetime.datetime(2023, 6, 15, 7, 26, 1, 411770, tzinfo=datetime.timezone.utc), upload_to='media/post/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 15, 7, 26, 12, 70036, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2023, 6, 15, 7, 26, 19, 177698, tzinfo=datetime.timezone.utc), editable=False, max_length=150, unique=True),
            preserve_default=False,
        ),
    ]
