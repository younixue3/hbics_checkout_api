from django.urls import path, include

from .views import ListApproval

urlpatterns = [
    path('cards/', ListApproval.as_view()),
]