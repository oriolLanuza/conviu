# Generated by Django 3.0.5 on 2020-04-22 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0003_auto_20200422_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='meetup_pic',
            field=models.ImageField(blank=True, upload_to='static/media/meetup_pics'),
        ),
    ]
