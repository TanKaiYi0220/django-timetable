from django.db.models.base import Model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, TimetableRow, TimetableElement

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class TimetableRowCreationForm(ModelForm):
    class Meta:
        model = TimetableRow
        fields = ['start', 'end']

class TimetableElementUpdateForm(ModelForm):
    class Meta:
        model = TimetableElement
        fields = ['body']