from django.contrib.auth.models import User, Group, auth
from rest_framework import viewsets, permissions, authentication, renderers, views, exceptions, pagination, generics
from quickstart.serializers import UserSerializer, GroupSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.http import HttpResponse
from django.views.decorators.http import require_GET


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()
        group = user.groups.all()
        groupserializer = GroupSerializer(group, many=True)
        if user is None:
            raise exceptions.AuthenticationFailed('User Not Found')

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Incorrect Password')

        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'name': user.first_name + ' ' +user.last_name,
            'group': groupserializer.data,
            'superuser': user.is_superuser
        })


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

@require_GET
def security_txt(request):
    lines = [
        "68E81249B074B3ADAB6F9D685F1B78364B2EA4D50109CA1FE5E46C43FD2D344D",
        "comodoca.com",
        "9b74ecfb7f969a0"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")