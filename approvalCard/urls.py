from django.urls import path, include

from .views import aprrovalList, aprrovalRecent, aprrovalSearch, aprrovalSearchStatus, aprrovalListForm, permissionPost

urlpatterns = [
    path('permissions/', aprrovalList),
    path('permission_recent/', aprrovalRecent),
    path('permission_search/', aprrovalSearch),
    path('permission_search/<str:uuid>', aprrovalSearchStatus),
    path('permissions_form/', aprrovalListForm),
    path('permission/apply', permissionPost)
]