from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup, Profile
from .serializers import MeetupSerializer
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    list_meetups=[]
    meetups_obj = Meetup.objects.all()
    for meetup in meetups_obj:
        list_meetups.append(MeetupSerializer(meetup).data)
    return render(request, 'meetups/index.html', context={'list_meetups':list_meetups},
    )

def profile(request, profile):
    return render(request, 'meetups/profile.html', context={'profile':profile,'profile_pic':get_pic(profile)}
    )

def addevent(request, profile):
    profile_obj = User.objects.get(username=profile)
    profile_pic = (str(profile_obj.profile.profile_pic)[7:])
    return render(request, 'meetups/addevent.html', context={'profile':profile,'profile_pic':get_pic(profile)}
    )


def get_pic(profile):
    profile_obj = User.objects.get(username=profile)
    return (str(profile_obj.profile.profile_pic)[7:])