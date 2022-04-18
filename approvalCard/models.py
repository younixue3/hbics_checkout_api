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
    permission_uuid = models.ManyToManyField(permissions, blank=True, null=True)
    user_uuid = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING
    )
