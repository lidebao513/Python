from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
def index(request):
    return HttpResponse('<h2><center>Hello XiaoBao！</center></h2>')

def douBan(request):
    movies = []
    for i in range(20):
        r=requests.get('https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=20')
        title = r.json()['subjects'][i]['title']
        rate = r.json()['subjects'][i]['rate']
        url = r.json()['subjects'][i]['url']
        cover = r.json()['subjects'][i]['cover']
        movies.append({
            'title': title,
            'rate': rate,
            'url': url,
            'cover': cover})
        print(movies)
    return render(request, 'laGou.html', locals())