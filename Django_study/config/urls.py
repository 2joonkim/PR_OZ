"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from http.client import responses

from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, Http404

movie_list = [
    {"title": "인사이드 아웃2", "director" : "켈시 만"},
    {"title": "데드풀과 울버린", "director" : "숀 레비"},
    {"title": "모아나 2", "director" : "데이비드 데릭 주니어 외 2명"},
    {"title": "슈퍼배드 4", "director" : "패트릭 델라지 외 1명"}
]

def index(request):
    return HttpResponse("<h1>HELL-LOW</h1>")

def book_list(request):

    book_text = ""

    for i in range(0, 10):
        book_text += f"book {i}<br>"

    return HttpResponse(book_text)

def book(request, num):
    book_text = f'book {num}번째 페이지입니다.'
    return HttpResponse(book_text)

def language(request, lang):
    return HttpResponse(f'<h1>{lang} 언어 페이지입니다.</h1>')

def movies(request):
    movie_titles = [
        f"<a href="/movies/{index}/">{movie['title']}</a>"
        for index, movie in enumerate(movie_list)
    ]
response_text = "<br>".join(movie_titles)
return HttpResponse(response_text)

def movie_detail(request, index):
    if index >= len(movie_list) -1:
        raise Http404

    response_text = f"<h1>영화 : {movies['title']}</h1>  <p>감독 : {movies['director']}</p>"
    return HttpResponse(response_text)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('book_list/', book_list),
    path('book_list/<int:num>/', book),
    path('language/<str:lang>/', language),
    path('movie/', movies),
    path('movie/<int:index>/', movie_detail),

]
