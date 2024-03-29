from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views
from .views import CustomAuthToken
from approvalCard.views import card_list
from approvalCard.views import CardsViewSet, PermissionViewSet

from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'cards', CardsViewSet)
router.register(r'permission', PermissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth', CustomAuthToken.as_view()),
    path('cards/', card_list),
    path('approvals/', include('approvalCard.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Note Install Pillow pip install pillow
