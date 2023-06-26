# django's default
from django.shortcuts import render

# knowark's addition
from django.urls import reverse_lazy
from django.views import generic
 
from .forms import CustomUserCreationForm

from django.db.models import Q

# 20230626 김경민 import, 모델 추가
from django.shortcuts import render
from django.http import HttpResponse
from .models import TotalnewsKT
from .models import TotalTKeyrank

import datetime
import pandas as pd
import re
from collections import Counter
from collections import OrderedDict
# close

# Create your views here.
# knowark's addition

# 20230626 main앱으로 옮김
def main (request) :
    # # 20230626 bar-chart
    # keywords = TotalTKeyrank.objects.values('keywords')
    # # print(type(keywords))
    # # print(posts)
    # w_list = []
    # for keyword in keywords:
    #     w = keyword.get('keywords')
    #     w_list.append(w)
    # # print(w_list)
    # cnts = TotalTKeyrank.objects.values('cnt')
    # # print(cnts)
    # c_list = []
    # for cnt in cnts:
    #     c = cnt.get('cnt')
    #     c_list.append(c)
    # # print(c_list)
    # w_c_list = []
    # for pair in zip(w_list, c_list):
    #     # print(pair)
    #     w_c_list.append(pair)
    # posts = pd.DataFrame(w_c_list, columns=['words, cnt'])
    # print(w_c_list)

    ## 20230626 line-chart
    date_n_keywords = TotalnewsKT.objects.filter().values_list('news_date','total_keywords')
    # print(date_n_keywords)

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


    # total_key_list
    # 년별로 집계하기
    # print(total_key_list) 
    # word_list = [] 
    # month_list = []
    # cnt_list = []
    # for tk in total_key_list:
    #     print(tk[0])
    #     print(tk[1])
    #     print(tk[2])
    #     month_list.append(tk[0])
    #     word_list.append(tk[1])
    #     cnt_list.append(tk[2])
        

    # 상위 순위 5개만
   
    list_w = []
    list_m_row = []
    list_cl_row = []
 
    for i in range(5):
        list_w.append(total_key_list[i][1])
        # 12개월치 카운트
        # 초기화
        list_m =[]
        list_cl = [] 
        
        for tk in total_key_list:
            list_m.append(tk[0])
            list_cl.append(tk[2])
        # 2차 리스트 생성
        list_m_row.append(list_m)
        list_cl_row.append(list_cl)
    print(list_w)
    # print(list_m_row)
    # print(list_cl_row)
    # print(word_list)
    # print(cloud_key_list)
    # "w_c_list":w_c_list, 
    #         "w_list":w_list, 
    #         "c_list":c_list, 
    print(list_cl_row[0])
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
            }
    return render(request, 'main.html', context)
# close


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('/')
    template_name = 'sign.html'




# class KeywordSearch() :
#     pass