
from django.urls import path, include
from . import views
 
urlpatterns = [
    # path('search/<str:q>/', views.KeywordSearch.as_view()),
    
    # path('accounts/sign/', views.SignUp.as_view(), name='sign'),
    path('sign/', views.SignUp.as_view(), name='sign'),
    # path('sign_success/', TemplateView.as_view(template_name='sign_success.html'), name='sign_success'),

    path('', views.main, name='lankings'),

    path('search/', views.search_news, name='search_news'),
    path('search/<str:keyword>/', views.search_news_by_keyword, name='search_results_by_keyword'),

    # path('#page2', views.post_view),
    
]