

from django.contrib.auth.forms import (UserCreationForm, UserChangeForm)
from .models import CustomUser
 
 
class CustomUserCreationForm(UserCreationForm):
 
    class Meta(UserCreationForm.Meta):
        model = CustomUser
<<<<<<< HEAD
        fields = ('username', 'email', 'career', 'career_keyword', 'affiliation')

        
    


=======
        fields = ('username', 'email', 'career', 'affiliation')
 
 
>>>>>>> 63140d75cb74c4abeacb41c98c57d6d40de94777
class CustomUserChangeForm(UserChangeForm):
 
    class Meta:
        model = CustomUser
<<<<<<< HEAD
        fields = ('username', 'email', 'career', 'career_keyword', 'affiliation')

=======
        fields = ('username', 'email', 'career', 'affiliation')
>>>>>>> 63140d75cb74c4abeacb41c98c57d6d40de94777
