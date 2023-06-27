

from django.contrib.auth.forms import (UserCreationForm, UserChangeForm)
from .models import CustomUser
 
 
class CustomUserCreationForm(UserCreationForm):
 
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'career', 'career_keyword', 'affiliation')
 
 
class CustomUserChangeForm(UserChangeForm):
 
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'career', 'career_keyword', 'affiliation')


