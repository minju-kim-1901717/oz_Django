"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('todo/', include('todo.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse, Http404
from django.urls import path
from django.shortcuts import render


movie_list = [
    {'title': '파묘', 'director': '장재현'},
    {'title': '범죄도시4 ', 'director': '허명행'},
    {'title': '인사이드 아웃 2', 'director': '켈시 만'},
    {'title': '베테랑2', 'director': '류승완'},
]

def index(request):
    return HttpResponse("Hello")

def blog_list(request):
    text = ''
    for i in range(0,10):
        text += f'book_{i}<br>'

    return HttpResponse(text)

def blog(request,num):
    text = f'book_{num}번 페이지 입니다'
    return HttpResponse(text)

def language(request,lang):
    return HttpResponse(f'{lang}언어 페이지 입니다')


def movies(request):
    # movie_titles = [movie['title'] for movie in movie_list]
    # response = ''
    # for index, title in enumerate(movie_titles):
    #     response += f'<a href="/movie/{index}">{title}</a><br>'
    # return HttpResponse(response)

    return render(request,'movies.html',{'movie_list': movie_list})

def movie_detail(request, index):
    if index > len(movie_list) -1:
        raise Http404
    movies = movie_list[index]
    return render(request, 'movie_detail.html', {'movie': movies})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    # path('todo/', blog_list),
    # path('todo/<int:num>/', todo),
    # path('language/<str:lang>/', language),
    path('movie/', movies),
    path('movie/<int:index>/', movie_detail),
]
