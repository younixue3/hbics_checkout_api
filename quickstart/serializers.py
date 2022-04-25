from django.contrib.auth.models import User, Group
from rest_framework import serializers

from approvalCard.models import cards, permissions


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        pagination_class = None

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        cardinser = cards(user_uuid_id=user.id)
        cardinser.save()
        return user

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
