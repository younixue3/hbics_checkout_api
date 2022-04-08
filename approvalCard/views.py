from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions as per
from .models import cards, permissions
from quickstart.serializers import CardsSerializer, PermissionsSerializer

class CardsViewSet(viewsets.ModelViewSet):
    queryset = cards.objects.all()
    serializer_class = CardsSerializer
    permission_classes = [per.IsAuthenticated]

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = permissions.objects.all()
    serializer_class = PermissionsSerializer
    permission_classes = [per.IsAuthenticated]

@api_view(['GET'])
def aprrovalList(request):
    if request.method == 'GET':
        card = cards.objects.all()
        serializer = CardsSerializer(card, many=True)
        return Response(serializer.data)
