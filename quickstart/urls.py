from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views
from .views import CustomAuthToken
<<<<<<< HEAD
from approvalCard.views import card_list
=======
from approvalCard.views import CardsViewSet, PermissionViewSet
>>>>>>> 46d1768ff0598756f664c4a0b6c67075df11f79b


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
<<<<<<< HEAD
=======
router.register(r'cards', CardsViewSet)
router.register(r'permission', PermissionViewSet)
>>>>>>> 46d1768ff0598756f664c4a0b6c67075df11f79b

urlpatterns = [
    path('', include(router.urls)),
    path('auth', CustomAuthToken.as_view()),
<<<<<<< HEAD
    path('cards/', card_list)
]
=======
    path('approvals/', include('approvalCard.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Note Install Pillow pip install pillow
>>>>>>> 46d1768ff0598756f664c4a0b6c67075df11f79b
