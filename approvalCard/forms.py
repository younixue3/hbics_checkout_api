from django import forms
from django.contrib.auth.models import User
from django.db.models import fields

class StaffForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'