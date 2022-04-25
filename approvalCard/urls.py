from django.urls import path, include

from .views import aprrovalList, aprrovalRecent, aprrovalSearch, aprrovalSearchStatus, aprrovalListForm, permissionPost, searchDetailStaff, searchLastDetailStaff, approvalPost, getLeader, permissionCheckIn, permissionCheckOut, userCreate

urlpatterns = [
    path('permissions/', aprrovalList),
    path('permission_recent/', aprrovalRecent),
    path('permission_search/', aprrovalSearch),
    path('permission_search/<str:uuid>', aprrovalSearchStatus),
    path('permissions_form/', aprrovalListForm),
    path('permission/apply', permissionPost),
    path('search_detail_staff/<int:id>', searchDetailStaff),
    path('search_last_detail_staff/<int:id>', searchLastDetailStaff),
    path('approval_post/<str:uuid>', approvalPost),
    path('get_leader/', getLeader),
    path('permissions_check/<str:uuid>', permissionCheckIn),
    path('permissions_check_out/<str:uuid>', permissionCheckOut),
    path('register', userCreate.as_view())
]