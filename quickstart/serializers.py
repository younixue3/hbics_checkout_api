from django.contrib.auth.models import User, Group
from rest_framework import serializers

from approvalCard.models import cards, permissions, authUserCard, authUserDivision, authDivision


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CardsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cards
        fields = ['id', 'permission_uuid']

class PermissionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = permissions
        field = ['id', 'description', 'created_at', 'updated_at', 'deleted_at']

class AuthUserCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = authUserCard
        field = ['id', 'card_uuid', 'user_uuid']

class AuthUserDivisionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = authUserDivision
        field = ['id', 'user_uuid', 'division_uuid', 'created_at', 'updated_at', 'deleted_at']

class AuthDivisionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = authDivision
        field = ['id', 'name']