# django's default
from django.shortcuts import render

# knowark's addition
from django.urls import reverse_lazy
from django.views import generic
 
from .forms import CustomUserCreationForm

from django.db.models import Q

import datetime
import pandas as pd
from .models import TotalTKeyrank, TotalTKeywordsRemake , TotalnewsKT, MainCustomuser, CustomUser, KeywordsTechworld, KeywordsRecentit, KeywordsItworld, KeywordsBloter, KeywordsCwn, KeywordsItbiz, RelatedKeywords
from .models import TotalnewsKT
from django.core.paginator import Paginator

# python으로 wordcloud 구현하기
from wordcloud import WordCloud
from collections import Counter

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
    # 230627 김경민 views 수정
    # key_connected in 통합 키워드 리스트 

    ## 20230626 김경민 bar-chart, line-chart
    ## 20230626 line-chart
    date_n_keywords = TotalnewsKT.objects.filter().values_list('news_date','total_keywords')
    # print(date_n_keywords)
    
    # 키워드
    date_list = []
    keyword_l = []
    for d_n_k in date_n_keywords:
        date = d_n_k[0]
        # object로 만들지 않으면 편집이 어려움
        date = date.strftime("%Y-%m-%d")
        date_list.append(date)
        key = d_n_k[1]
        keyword_l.append(key)


    # print(date_list, keyword_l) 

    # 월별로 집계하기
    # 모듈화하기
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
    # 날짜 정순이 되게끔 뒤집기
    total_key_list = total_key_list[::-1]

    # 상위 순위 5개만
    list_m_row = []
    list_w = []
    list_cl_row = []

    for i in range(5):
        list_w.append(total_key_list[i][1])
        # 12개월치 카운트
        # 초기화
        list_m = []
        list_cl = [] 
        
        for tk in total_key_list:
            if tk[1] == total_key_list[i][1]:
                list_m.append(tk[0])
                list_cl.append(tk[2])
            else:
                pass
        # 2차 리스트 생성
        list_m_row.append(list_m)
        list_cl_row.append(list_cl)

        
    



    # 230627 왕예슬 통합
    context = {
        "month_list_0":list_m_row[0],
        "month_list_1":list_m_row[1],
        "month_list_2":list_m_row[2],
        "month_list_3":list_m_row[3],
        "month_list_4":list_m_row[4],
        "key_list":list_w,
        "cnt_list_0":list_cl_row[0],
        "cnt_list_1":list_cl_row[1],
        "cnt_list_2":list_cl_row[2],
        "cnt_list_3":list_cl_row[3],
        "cnt_list_4":list_cl_row[4],
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

    global total_rankings, bloter_rankings, cwn_rankings, itbiz_rankings, itworld_rankings, yozmit_rankings, techworld_rankings, jr_keywords, sr_keywords, w_c_list, w_list, c_list, cloud_key_list, month_list, cnt_list

def search_news(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword') 
        news_list = TotalnewsKT.objects.filter(news_title__icontains=keyword)
        context = {'news_list': news_list}
        return render(request, 'search_results.html', context)

    
def search_news_by_keyword(request, keyword):

    global total_rankings, bloter_rankings, cwn_rankings, itbiz_rankings, itworld_rankings, yozmit_rankings, techworld_rankings, jr_keywords, sr_keywords, w_c_list, w_list, c_list, cloud_key_list, month_list, cnt_list
    
    
    news_list = TotalnewsKT.objects.filter(news_title__icontains=keyword)
    

    # print(keyword)
    # 페이지당 10개씩
    items_per_page = 10

    # # 20글자 // 이후에는 ... 으로 표시
    # news_list = [news if len(news.news_title) <= 20 else news.news_title[:17] + "..." for news in news_list]

    ##### 20230627 김경민 검색창-챠트 연동 기능 통합
    date_n_keywords = TotalnewsKT.objects.filter().values_list('news_date','total_keywords')
    # print(date_n_keywords)
    
    
    # 키워드
    date_list = []
    keyword_l = []
    for d_n_k in date_n_keywords:
        date = d_n_k[0]
        # object로 만들지 않으면 편집이 어려움
        date = date.strftime("%Y-%m-%d")
        key = d_n_k[1] # str
        # print(date,key) 
        # keyword_l.append(key)
        ### 20230627 김경민 keyword를 읽고 리스트 출력
        

        if keyword == '프로그래밍':
            # print(key)
            key = key.split(",")
            # print(key)
            if '프로그래밍' in key or '노트북' in key or '언어' in key or '추천' in key or '자바' in key or '자격증' in key or '웹' in key or '개발' in key or '프레임워크' in key or '지능' in key or '주목' in key or '클라우드' in key:
                date_list.append(date)
                key = ','.join(key)
                keyword_l.append(key)
            else:
                pass
        

        elif keyword == '트렌드':
            key = key.split(",")
            if '트렌드' in key or '분석' in key or '소비' in key or '투자' in key or '인기' in key or '데이터' in key or '개발' in key or '공개' in key or '규모' in key or '메타' in key or '솔루션' in key or '유치' in key:
                date_list.append(date)
                key = ','.join(key)
                keyword_l.append(key)
            else:
                pass
        
        elif keyword == '코드':
            key = key.split(",")
            if '코드' in key or '네이버' in key or '트렌드' in key or '인기' in key or '언어' in key or '서비스' in key or '플랫폼' in key or '업체' in key or '카드' in key or '기사' in key or '데이터' in key  or '보안' in key  or '관리' in key  or '웹' in key or '선정' in key or '기반' in key or '코드' in key or '웨어' in key or '연구' in key or '지원' in key or '네트워크' in key or '관리' in key or '발표' in key:

    related_words = ""
    wordcloud_link = 'wordcloud'
    # 연관어 목록 불러오기
    if keyword == '프로그래밍':
        related_words = RelatedKeywords.objects.filter(words__icontains='프로그래밍').values_list('related', flat=True)
        wordcloud_link = 'computer_lang'
    elif keyword == '트렌드':
        related_words = RelatedKeywords.objects.filter(words__icontains='트렌드').values_list('related', flat=True)
        wordcloud_link = 'computer_pop'
    elif keyword == '코드':
        related_words = RelatedKeywords.objects.filter(words__icontains='코딩').values_list('related', flat=True)
        wordcloud_link = 'computer_code'
    else:
        related_words = RelatedKeywords.objects.filter().values_list('related')
        wordcloud_link = 'wordcloud'


    # 월별로 집계하기
    # 모듈화하기
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
            # 불용어 처리
            filtered_counts = [(word, count) for word, count in sorted_counts if word not in ['체결','가지','기반','티', '지수']]
            
            # 만약 2이상인 단어의 수가 20개 미만이면 모든 단어 추출
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
    # 날짜 정순이 되게끔 뒤집기
    total_key_list = total_key_list[::-1]

    # 상위 순위 5개만
    list_m_row = []
    list_w = []
    list_cl_row = []

    for i in range(5):
        list_w.append(total_key_list[i][1])
        # 12개월치 카운트
        # 초기화
        list_m = []
        list_cl = [] 
        
        for tk in total_key_list:
            if tk[1] == total_key_list[i][1]:
                list_m.append(tk[0])
                list_cl.append(tk[2])
            else:
                pass
        # 2차 리스트 생성
        list_m_row.append(list_m)
        list_cl_row.append(list_cl)

    

    # 5 -> 다음
    paginator = Paginator(news_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # string화
 
    print(related_words)
    related_words = related_words[0].split(",")
    # related_words = related_words.split(",")
    n = 0
    related_words_odd = []
    related_words_even = []
    for w in related_words:
        if n % 2 != 0:
            related_words_odd.append(w)
        if n % 2 == 0:
            related_words_even.append(w)
        n += 1

    checkres = 1

    context = {
        #### 230627 김경민 검색창과 연동
        "month_list_0":list_m_row[0],
        "month_list_1":list_m_row[1],
        "month_list_2":list_m_row[2],
        "month_list_3":list_m_row[3],
        "month_list_4":list_m_row[4],
        "key_list":list_w,
        "cnt_list_0":list_cl_row[0],
        "cnt_list_1":list_cl_row[1],
        "cnt_list_2":list_cl_row[2],
        "cnt_list_3":list_cl_row[3],
        "cnt_list_4":list_cl_row[4],
        "related_words_odd":related_words_odd,
        "related_words_even":related_words_even,
        "wordcloud_link":wordcloud_link,
        #### 230627 김경민 close
        'news_list': page_obj,
        'keyword': keyword,
        # 신호 확인용
        "checkres": checkres,
        #### 230627 김경민 close
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
    # 20230627 김경민 검색창-챠트 연동 기능 통합 close

    
    return render(request, 'search_results.html', context)







