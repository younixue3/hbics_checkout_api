from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

class cards(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False),
    permission_uuid = models.ForeignKey(
        'permissions',
        on_delete=models.DO_NOTHING,
    ),

class permissions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False),
    description = models.TextField(),
    created_at = models.DateTimeField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True),
    deleted_at = models.DateTimeField(auto_now=False, auto_now_add=False, )

class authUserCard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False),
    card_uuid = models.ForeignKey(
        'cards',
        on_delete=models.DO_NOTHING,
    ),
    user_uuid = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING
    ),

class authUserDivision(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False),
    user_uuid = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING
    ),
    division_uuid = models.ForeignKey(
        'authDivision',
        on_delete=models.DO_NOTHING
    ),
    created_at = models.DateTimeField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True),
    deleted_at = models.DateTimeField()

class authDivision(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False),
    name = models.CharField(max_length=15)