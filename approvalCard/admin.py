from django.contrib import admin
from .models import cards, permissions

admin.site.register([cards, permissions])
