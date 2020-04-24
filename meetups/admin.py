from django.contrib import admin

from .models import Profile, Meetup, Category

admin.site.register(Profile)
admin.site.register(Meetup)
admin.site.register(Category)

# Register your models here.
