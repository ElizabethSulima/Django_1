from django.shortcuts import render

from .models import Article


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.order_by('-published_at')
    return render(request, template, {'articles': articles})
