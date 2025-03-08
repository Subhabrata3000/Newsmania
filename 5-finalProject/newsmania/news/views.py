from django.shortcuts import render
from .models import NewsVarity
from django.shortcuts import get_object_or_404

# Create your views here.
def all_news(request):
    all_news = NewsVarity.objects.all()
    return render(request, 'all_news.html', {'all_news': all_news})

def news_details(request, news_id):
    one_news = get_object_or_404(NewsVarity, pk = news_id)
    return render(request, 'news_details.html', {'news': one_news})
