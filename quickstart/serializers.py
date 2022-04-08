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
        fields = ['url', 'name']

class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = cards
        fields = ['url', 'id', 'user_uuid_id']
        pagination_class = None

class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = permissions
        fields = ['url', 'description', 'status', 'created_at', 'updated_at', 'deleted_at']
        pagination_class = None