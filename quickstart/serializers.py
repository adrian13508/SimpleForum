from django.contrib.auth.models import User, Group
from django.utils.module_loading import import_string
from .models import Post, Like
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Post
        fields = "__all__"