from rest_framework import serializers
from .models import Meetup, Category, Profile
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class ProfileSerializer(serializers.ModelSerializer):
    username = UserSerializer()
    class Meta:
        model = Profile
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class MeetupSerializer(serializers.ModelSerializer):
    username = UserSerializer()
    category = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Meetup
        fields = "__all__"

