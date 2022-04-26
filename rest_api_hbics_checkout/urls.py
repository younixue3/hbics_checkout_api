from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from quickstart import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('quickstart.urls')),
    path('.well-known/pki-validation/BCBF73E9CBC31B88553006273C32FE3E.txt', views.security_txt)
]