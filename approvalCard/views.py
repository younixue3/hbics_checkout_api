from django.shortcuts import render
from rest_framework import viewsets, response, status
from rest_framework.decorators import api_view
from rest_framework import permissions as per
from .models import cards, authDivision, authUserDivision, authUserCard, permissions
from quickstart.serializers import CardsSerializer, PermissionsSerializer, AuthUserCardSerializer, AuthUserDivisionSerializer, AuthDivisionSerializer

# class CardsViewSet(viewsets.ModelViewSet):
#     queryset = cards.objects.all()
#     serializer_class = CardsSerializer
#     permission_classes = [per.IsAuthenticated]

def card_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = cards.objects.all()
        serializer = CardsSerializer(snippets, many=True)
        return response.Response(serializer.data)
