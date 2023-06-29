# django's default
from django.shortcuts import render, redirect

# knowark's addition
from django.urls import reverse_lazy
from django.views import generic
 
from .forms import CustomUserCreationForm

from django.db.models import Q

# 동석추가
from .models import TotalnewsKT
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger


# Create your views here.
# knowark's addition
def main (request) :
    return render (request, 'main.html')



class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('/')
    template_name = 'sign.html'

def search_news(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        return redirect('search_results_by_keyword', keyword=keyword)
    else:
        return render(request, 'search_form.html')

def search_results_by_keyword(request, keyword):
    
    news_list = TotalnewsKT.objects.filter(news_title__icontains=keyword)
    paginator = Paginator(news_list, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    context = {
        'news_list': page_obj,
        'keyword': keyword,
    }
    return render(request, 'search_results.html', context)