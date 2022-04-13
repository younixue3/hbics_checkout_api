from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions as per
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, Group, auth
from .models import cards, permissions
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.renderers import JSONRenderer
from quickstart.serializers import CardsSerializer, PermissionsSerializer, CardsListSerializer
from django.db.models import Q

class CardsViewSet(viewsets.ModelViewSet):
    queryset = cards.objects.all()
    serializer_class = CardsSerializer
    permission_classes = [per.IsAuthenticated]

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = permissions.objects.all()
    serializer_class = PermissionsSerializer
    permission_classes = [per.IsAuthenticated]

@api_view(['POST'])
def aprrovalList(request):
    if request.method == 'POST':
        token_user = Token.objects.get(key=request.data['token']).user
        user_id = User.objects.get(username=token_user).id
        card = cards.objects.get(user_uuid_id__id=user_id)
        # print()
        permissionlist = card.permission_uuid.order_by('-created_at')[1:]
        serializer = PermissionsSerializer(permissionlist, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def aprrovalListForm(request):
    if request.method == 'POST':
        token_user = Token.objects.get(key=request.data['token']).user
        user_id = User.objects.get(username=token_user).id
        card = cards.objects.get(user_uuid_id__id=user_id)
        permissionlist = card.permission_uuid.all()
        serializer = PermissionsSerializer(permissionlist, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def aprrovalSearch(request):
    if request.method == 'POST':
        groupdata = Group.objects.get(name=request.data['group'][1]['name'])
        user_id = User.objects.filter(Q(groups__name__in=[groupdata]) and Q(groups__name__in=['Staff']))
        card = cards.objects.filter(Q(user_uuid__groups__name__in=[groupdata]) and Q(user_uuid__groups__name__in=['Staff'])).all()
        serializer = CardsSerializer(card, many=True)
        return Response(serializer.data)

        # print(request.data['group'])
        # for i in request.data['group']:

@api_view(['POST'])
def aprrovalSearchStatus(request, uuid):
    if request.method == 'POST':
        print(uuid)
        permissiondata = permissions.objects.get(id=uuid)
        print(permissiondata)
        serializer = PermissionsSerializer(permissiondata)
        return Response(serializer.data)

        # print(request.data['group'])
        # for i in request.data['group']:


            # print(i['name'])
        # token_user = Token.objects.get(key=request.data['token']).user
        # user_id = User.objects.get(username=token_user).id
        # card = cards.objects.get(user_uuid_id__id=user_id)
        # permissionlist = card.permission_uuid.filter(Q(status='RJ') | Q(status='AC')).all()[1:]
        # serializer = PermissionsSerializer(permissionlist, many=True)
        # return Response(serializer.data)

@api_view(['POST'])
def aprrovalRecent(request):
    if request.method == 'POST':
        token_user = Token.objects.get(key=request.data['token']).user
        user_id = User.objects.get(username=token_user).id
        card = cards.objects.get(user_uuid_id__id=user_id)
        permissionrecent = card.permission_uuid.order_by('-created_at')[0:1]
        serializer = PermissionsSerializer(permissionrecent, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def permissionPost(request):
    if request.method == 'POST':
        token_user = Token.objects.get(key=request.data['token']).user
        user_id = User.objects.get(username=token_user).id
        card = cards.objects.get(user_uuid_id__id=user_id)
        # print(card.permission_uuid.first())
        if card.permission_uuid.first() == None:
            serializer_permission = PermissionsSerializer(data=request.data)
            if serializer_permission.is_valid():
                permission_id = serializer_permission.save().id
                card.permission_uuid.add(permission_id)
                context = {'error': True, 'massage': 'Izin terakhir anda masih di proses'}
                return Response(context)
        else:
            if card.permission_uuid.last().status == 'NO':
                context = {'error': True, 'massage': 'Izin terakhir anda masih di proses'}
                return Response(context)
            else:
                serializer_permission = PermissionsSerializer(data=request.data)
                if serializer_permission.is_valid():
                    permission_id = serializer_permission.save().id
                    card.permission_uuid.add(permission_id)
                    context = {'error': True, 'massage': 'Izin terakhir anda masih di proses'}
                    return Response(context)
        # print(serializer_permission.save())

#####################################
#### MULTIPLE OUTPUT SERIALIZERS ####
#####################################
# @api_view(['POST'])
# def aprrovalList(request):
#     if request.method == 'POST':
#         token_user = Token.objects.get(key=request.data['token']).user
#         user_id = User.objects.get(username=token_user).id
#         card = cards.objects.get(user_uuid_id__id=user_id)
#         permissionrecent = card.permission_uuid.all()[1:2]
#         permissionlist = card.permission_uuid.all()[1:]
#         serializer_recent = PermissionsSerializer(permissionrecent, many=True)
#         serializer_list = PermissionsSerializer(permissionlist, many=True)
#         serializer = serializer_recent.data + serializer_list.data
#         print(serializer)
#         context = {'list': serializer_list.data, 'recent': serializer_recent.data}
#         return Response(context)
