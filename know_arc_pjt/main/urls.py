
from django.urls import path
from django.views.generic import TemplateView
from . import views
 
urlpatterns = [
    # path('search/<str:q>/', views.KeywordSearch.as_view()),
    
    # path('accounts/sign/', views.SignUp.as_view(), name='sign'),
    path('sign/', views.SignUp.as_view(), name='sign'),
    # path('sign_success/', TemplateView.as_view(template_name='sign_success.html'), name='sign_success'),
]