from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions as per
from .models import cards, authDivision, authUserDivision, authUserCard, permissions
from quickstart.serializers import CardsSerializer, PermissionsSerializer, AuthUserCardSerializer, AuthUserDivisionSerializer, AuthDivisionSerializer

class CardsViewSet(viewsets.ModelViewSet):
    queryset = cards.objects.all()
    serializer_class = CardsSerializer
    permission_classes = [per.IsAuthenticated]