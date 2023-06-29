# django's default
from django.shortcuts import render

# knowark's addition
from django.urls import reverse_lazy
from django.views import generic
 
from .forms import CustomUserCreationForm

from django.db.models import Q

import datetime
import pandas as pd
from .models import TotalTKeyrank, TotalnewsKT, MainCustomuser, CustomUser, KeywordsTechworld, KeywordsRecentit, KeywordsItworld, KeywordsBloter, KeywordsCwn, KeywordsItbiz
from .models import TotalnewsKT
from django.core.paginator import Paginator



# Create your views here.
# knowark's addition
def main (request) :

    global total_rankings, bloter_rankings, cwn_rankings, itbiz_rankings, itworld_rankings, yozmit_rankings, techworld_rankings, jr_keywords, sr_keywords, w_c_list, w_list, c_list, cloud_key_list, month_list, cnt_list

    ############## ranking part
    total_rankings = TotalTKeyrank.objects.all().order_by('idx')[:10]
    bloter_rankings = KeywordsBloter.objects.all().order_by('idx')[:10]
    cwn_rankings = KeywordsCwn.objects.all().order_by('idx')[:10]
    itbiz_rankings = KeywordsItbiz.objects.all().order_by('idx')[:10]
    itworld_rankings = KeywordsItworld.objects.all().order_by('idx')[:10]
    yozmit_rankings = KeywordsRecentit.objects.all().order_by('idx')[:10]
    techworld_rankings = KeywordsTechworld.objects.all().order_by('idx')[:10]

    ############## versus part
    jr_keywords = CustomUser.objects.filter(career='주니어').values('career_keyword').distinct()
    sr_keywords = CustomUser.objects.filter(career='시니어').values('career_keyword').distinct()
    # print(jr_keywords)
    # print(sr_keywords)

    ############## chart part
    keywords = TotalTKeyrank.objects.values('keywords')
    cnts = TotalTKeyrank.objects.values('cnt')
    date_n_keywords = TotalnewsKT.objects.filter().values_list('news_date','total_keywords')

    
    w_list = []
    for keyword in keywords:
        w = keyword.get('keywords')
        w_list.append(w)

    c_list = []
    for cnt in cnts:
        c = cnt.get('cnt')
        c_list.append(c)

    w_c_list = []
    for pair in zip(w_list, c_list):
        # print(pair)
        w_c_list.append(pair)

    date_list = []
    keyword_l = []
    for d_n_k in date_n_keywords:
        date = d_n_k[0]
        date = date.strftime("%Y-%m-%d")
        date_list.append(date)
        key = d_n_k[1]
        keyword_l.append(key)


    def get_keyword_monthly_agg(keyword_l, date_list):
        text_data = keyword_l
        date_data = date_list
        
        
        # 단어 등장 횟수를 저장할 딕셔너리 초기화
        word_counts = {}
        # 월별 단어 집계
        word_n_cnt_list = []
        
        # 데이터프레임을 순회하며 월 별로 단어 등장 횟수 집계
        for text, date in zip(text_data, date_data):
            # 텍스트 토큰화 및 형태소 분석
            
            # 년 추출
            tokens = text.split(",")
            year = date.split('-')[0]
            # 월 추출
            month = date.split('-')[1]
            year_month = year + '-' + month

            # 단어 등장 횟수 집계
            if year_month in word_counts:
                for token in tokens:
                    word_counts[year_month][token] = word_counts[year_month].get(token, 0) + 1
            else:
                word_counts[year_month] = {}
                for token in tokens:
                    word_counts[year_month][token] = 1
                    
        # 횟수가 2이상인 단어만 추출하기
        min_word_count = 2
        top_words_limit = 21 # 최대 20개
        
        # 월 별로 상위 단어 추출
        
        for year_month, counts in word_counts.items():
            # print(f"{month}월")
            # 횟수만 추출하기
            sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
            
            # 횟수가 2이상인 단어 필터링
            filtered_counts = [(word, count) for word, count in sorted_counts if count >= min_word_count]
            
            # 만약 2이상인 단어의 수가 5개 미만이면 모든 단어 추출
            if len(filtered_counts) < top_words_limit:
                filtered_counts = sorted_counts
            # 상위 단어 출력
            top_words = filtered_counts[:top_words_limit]
            for word, count in top_words:
                # print(f" {word} | 등장횟수: {count}")
                word_n_cnt_list.append([year_month, word, count])
            # print(word_n_cnt_list)
            # print()
        
        return word_n_cnt_list

    total_key_list = get_keyword_monthly_agg(keyword_l, date_list)
    total_key_list = total_key_list[::-1]


    cloud_key_list = [] 
    month_list = []
    cnt_list = []
    for tk in total_key_list:
        if tk[1] == '클라우드':
            print(tk[0])
            print(tk[1])
            print(tk[2])
            cloud_key_list.append(tk)
            month_list.append(tk[0])
            cnt_list.append(tk[2])
        else:
            pass
    # print(cloud_key_list)



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
        "w_c_list":w_c_list, 
        "w_list":w_list, 
        "c_list":c_list,
        "total_key_list":cloud_key_list,
        "month_list":month_list,
        "cnt_list":cnt_list
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
        "w_c_list":w_c_list, 
        "w_list":w_list, 
        "c_list":c_list,
        "total_key_list":cloud_key_list,
        "month_list":month_list,
        "cnt_list":cnt_list
    }
    

    
    return render(request, 'search_results.html', context)







