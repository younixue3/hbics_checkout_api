from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views
from .views import CustomAuthToken
from approvalCard.views import CardsViewSet


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'cards', CardsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth', CustomAuthToken.as_view()),
]