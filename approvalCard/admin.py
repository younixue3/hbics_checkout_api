from django.contrib import admin
from .models import cards, permissions, authUserCard, authUserDivision, authDivision

admin.site.register([cards, permissions, authUserCard, authUserDivision, authDivision])
