from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions as per
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, Group, auth
from .models import cards, permissions
from rest_framework.renderers import JSONRenderer
from quickstart.serializers import CardsSerializer, PermissionsSerializer, CardsListSerializer

class CardsViewSet(viewsets.ModelViewSet):
    queryset = cards.objects.all()
    serializer_class = CardsSerializer
    permission_classes = [per.IsAuthenticated]

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = permissions.objects.all()
    serializer_class = PermissionsSerializer
    permission_classes = [per.IsAuthenticated]

# @api_view(['POST'])
# def aprrovalList(request):
#     if request.method == 'POST':
#         token_user = Token.objects.get(key=request.data['token']).user
#         user_id = User.objects.get(username=token_user).id
#         card = cards.objects.get(user_uuid_id__id=user_id)
#         permissionss = {'data': []}
#         permission = card.permission_uuid.all()
#         for value in permission:
#             permissionss['data'].append(permissions.objects.values('description', 'status').get(id=value.id))
#         print(permissionss['data'])
#         serializer = CardsListSerializer(card)
#         context = {'card': serializer.data, 'permissions': permissions}
#         return Response(serializer.data)
# @api_view(['POST'])
class ListApproval(APIView):
    cardprimary = ''

    def post(self, request, *args, **kwargs):
        token_user = Token.objects.get(key=request.data['token']).user
        user_id = User.objects.get(username=token_user).id
        card = cards.objects.get(user_uuid_id__id=user_id)

        permissionss = {'data': []}
        permission = card.permission_uuid.all()
        for value in permission:
            permissionss['data'].append(permissions.objects.values('description', 'status').get(id=value.id))
        print(permissionss['data'])
        serializer = CardsListSerializer(card)
        context = {'card': serializer.data, 'permissions': permissions}
        return Response(serializer.data)

