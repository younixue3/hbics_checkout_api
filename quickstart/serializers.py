from django.contrib.auth.models import User, Group
from rest_framework import serializers

from approvalCard.models import cards, permissions


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        pagination_class = None


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        pagination_class = None

class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = cards
        fields = '__all__'
        pagination_class = None

class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = permissions
        fields = '__all__'
        pagination_class = None

class CardsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = cards
        fields = '__all__'
        pagination_class = None
