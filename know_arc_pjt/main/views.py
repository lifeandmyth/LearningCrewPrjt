# django's default
from django.shortcuts import render

# knowark's addition
from django.urls import reverse_lazy
from django.views import generic
 
from .forms import CustomUserCreationForm

from django.db.models import Q



# Create your views here.
# knowark's addition
def main (request) :
    return render (request, 'main.html')



class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('/')
    template_name = 'sign.html'



# class KeywordSearch() :
#     pass