from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")
def post_view(request):
    posts = Post.objects.all() #Post테이블의 모든 객체 불러와서 posts변수에 저장
    print(posts)
    return render(request, 'index.html', {"posts", posts})
