from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

class permissions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    REJECT = 'RJ'
    ACCEPT = 'AC'
    DONE = 'DN'
    OUTSIDE = 'OU'
    NOT_YET = 'NO'
    STATUS_CHOICES = [
        (REJECT, 'Reject'),
        (ACCEPT,'Accept'),
        (DONE, 'Done'),
        (OUTSIDE, 'Outside'),
        (NOT_YET, 'Not Yet'),
    ]
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=NOT_YET
    )
    appoval_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

class cards(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
<<<<<<< HEAD
    permission_uuid = models.ManyToManyField(permissions)

class authUserCard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    card_uuid = models.ForeignKey(
        'cards',
        on_delete=models.DO_NOTHING,
    )
=======
    permission_uuid = models.ManyToManyField(permissions, blank=True, null=True)
>>>>>>> 46d1768ff0598756f664c4a0b6c67075df11f79b
    user_uuid = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING
    )

<<<<<<< HEAD
class authUserDivision(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
=======
class profile_pic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    namefile = models.TextField()
>>>>>>> 46d1768ff0598756f664c4a0b6c67075df11f79b
    user_uuid = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING
    )
    created_at = models.DateTimeField(auto_now_add=True)
<<<<<<< HEAD
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

class authDivision(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=15)
=======
    deleted_at = models.DateTimeField(blank=True, null=True)
>>>>>>> 46d1768ff0598756f664c4a0b6c67075df11f79b
