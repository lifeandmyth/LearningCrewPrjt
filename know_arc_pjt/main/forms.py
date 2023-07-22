

from django.contrib.auth.forms import (UserCreationForm, UserChangeForm)
from .models import CustomUser, MainCustomuser
 
 
class CustomUserCreationForm(UserCreationForm):
 
    # class Meta(UserCreationForm.Meta):
    #     model = CustomUser
    #     fields = ('username', 'email', 'career', 'career_keyword', 'affiliation')
    class Meta(UserCreationForm.Meta):
        model = MainCustomuser
        fields = ('username', 'email', 'career', 'career_keyword', 'affiliation')

        
    


class CustomUserChangeForm(UserChangeForm):
 
    # class Meta:
    #     model = CustomUser
    #     fields = ('username', 'email', 'career', 'career_keyword', 'affiliation')
    class Meta:
        model = MainCustomuser
        fields = ('username', 'email', 'career', 'career_keyword', 'affiliation')

