from django.shortcuts import render
from django.http import HttpResponse
from .models import NewsSites
from .models import NewsTechworldT


# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")
def post_view(request):
    posts = NewsSites.objects.all() #NewsSites테이블의 모든 객체 불러와서 posts변수에 저장
    #여기서 NewsTechworldT테이블의 데이터도 가져와서 dict 안에 넣는다
    print(posts)
    return render(request, 'index.html', {"posts": posts})
