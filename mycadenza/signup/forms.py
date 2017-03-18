from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CadenzaUser

class CadenzaUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CadenzaUser
        fields = ('email', 'mobile')
        error_css_class = 'error'
