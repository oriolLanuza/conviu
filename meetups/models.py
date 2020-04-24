from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import date, timedelta
from django.db.models.fields import DateTimeField, DurationField

class Category(models.Model):
    name = models.CharField(max_length=200, help_text="Escriu la categoria de l'esdeveniment.")
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to='static/media/profile_pics',blank=True)

    def __str__(self):
        return self.username.username

class Meetup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID unic per aquest esdeveniment")
    title = models.CharField(max_length=30)
    username = models.ForeignKey('Profile', on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)
    url = models.URLField(max_length = 200)
    category = models.ManyToManyField(Category, help_text="Selecciona la categoria d'aquest esdeveniment.")
    start = models.DateTimeField()
    duration = models.DurationField(default=timedelta(hours=1))
    meetup_pic = models.ImageField(upload_to='static/media/meetup_pics',blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["start"]

    @property
    def is_online(self):
        if ((self.start < date.now()) and (date.now() < self.end)):
            return True
        return False