# django's default
from django.shortcuts import render

# knowark's addition
from django.urls import reverse_lazy
from django.views import generic
 
from .forms import CustomUserCreationForm

from django.db.models import Q

import pandas as pd
from .models import TotalTKeyrank, MainCustomuser, CustomUser, KeywordsTechworld, KeywordsRecentit, KeywordsItworld, KeywordsBloter, KeywordsCwn, KeywordsItbiz
from .models import TotalnewsKT
from django.core.paginator import Paginator



# Create your views here.
# knowark's addition
def main (request) :

    global total_rankings, bloter_rankings, cwn_rankings, itbiz_rankings, itworld_rankings, yozmit_rankings, techworld_rankings, jr_keywords, sr_keywords

    total_rankings = TotalTKeyrank.objects.all().order_by('idx')[:10]
    bloter_rankings = KeywordsBloter.objects.all().order_by('idx')[:10]
    cwn_rankings = KeywordsCwn.objects.all().order_by('idx')[:10]
    itbiz_rankings = KeywordsItbiz.objects.all().order_by('idx')[:10]
    itworld_rankings = KeywordsItworld.objects.all().order_by('idx')[:10]
    yozmit_rankings = KeywordsRecentit.objects.all().order_by('idx')[:10]
    techworld_rankings = KeywordsTechworld.objects.all().order_by('idx')[:10]




    jr_keywords = CustomUser.objects.filter(career='주니어').values('career_keyword').distinct()
    sr_keywords = CustomUser.objects.filter(career='시니어').values('career_keyword').distinct()
    # print(jr_keywords)
    # print(sr_keywords)
    context = {
        'total_rankings' : total_rankings, 
        'bloter_rankings' : bloter_rankings,
        'cwn_rankings' : cwn_rankings,
        'itbiz_rankings' : itbiz_rankings,
        'itworld_rankings' : itworld_rankings,
        'yozmit_rankings' : yozmit_rankings,
        'techworld_rankings' : techworld_rankings,
        'jr_keywords' : jr_keywords, 
        'sr_keywords' : sr_keywords,
        }
    
    # print(artcs)
    return render (request, 'main.html', context)




class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('/')
    template_name = 'sign.html'



def search_news(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword') 
        news_list = TotalnewsKT.objects.filter(news_title__icontains=keyword)
        context = {'news_list': news_list}
        return render(request, 'search_results.html', context)
    else:
        return render(request, 'search_form.html')
    
def search_news_by_keyword(request, keyword):
    news_list = TotalnewsKT.objects.filter(news_title__icontains=keyword)
    
    # 페이지당 10개씩
    items_per_page = 10

    # # 20글자 // 이후에는 ... 으로 표시
    # news_list = [news if len(news.news_title) <= 20 else news.news_title[:17] + "..." for news in news_list]

    # 5 -> 다음
    paginator = Paginator(news_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'news_list': page_obj,
        'keyword': keyword,
        'total_rankings' : total_rankings, 
        'bloter_rankings' : bloter_rankings,
        'cwn_rankings' : cwn_rankings,
        'itbiz_rankings' : itbiz_rankings,
        'itworld_rankings' : itworld_rankings,
        'yozmit_rankings' : yozmit_rankings,
        'techworld_rankings' : techworld_rankings,
        'jr_keywords' : jr_keywords, 
        'sr_keywords' : sr_keywords,
    }

    
    return render(request, 'search_results.html', context)