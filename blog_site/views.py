import requests
from django.shortcuts import render, get_object_or_404
from blog_api.models import BlogArticle


def home(request):
    return render(request, 'nav/home.html')


def contributions(request):
    return render(request, 'nav/contributions.html')


def blog(request):
    api_url = 'http://localhost:8000/api/blog/all/'  # Update the API URL
    response = requests.get(api_url)

    if response.status_code == 200:
        blog_articles = response.json()
    else:
        blog_articles = []

    context = {
        'blog_articles': blog_articles
    }

    return render(request, 'nav/blog.html', context)


def article_details(request, article_id):
    article = get_object_or_404(BlogArticle, pk=article_id)
    return render(request, 'article/details.html', {'article': article})
