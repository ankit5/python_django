from rest_framework import serializers
from .models import Book

from django.contrib.auth.models import User, Group

# Create a model serializer
class BookSerializer(serializers.ModelSerializer):
  # specify model and fields
   class Meta:
       model = Book
       fields = ('title', 'description')


class BookSerializerId(serializers.ModelSerializer):
  # specify model and fields
   class Meta:
       model = Book
       fields = ('id', 'description')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']