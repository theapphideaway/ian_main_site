import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView

from blog_api.models import BlogArticle
from blog_site.forms import BlogArticleForm


def home(request):
    return render(request, 'nav/home.html')


def contributions(request):
    return render(request, 'nav/contributions.html')


def blog(request):
    api_path = '/api/blog/all/'  # API endpoint path
    api_url = f"{request.scheme}://{request.get_host()}{api_path}"  # Construct API URL dynamically
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


class CreateArticleView(TemplateView):
    template_name = 'article/create_article.html'


import requests

def add_blog_article(request):
    if request.method == 'POST':
        form = BlogArticleForm(request.POST)
        if form.is_valid():
            # Prepare data to send to the API
            api_data = {
                "title": form.cleaned_data['title'],
                "date_published": form.cleaned_data['date_published'],
                "tag": form.cleaned_data['tag'],
                "content": form.cleaned_data['content']
            }

            # Send data to the API endpoint
            response = requests.post('http://localhost:8000/api/add-blog/', json=api_data)

            if response.status_code == 201:
                # Successfully created
                return redirect('blog')
            else:
                # Handle the case where the request failed
                print('Request Failed')
    else:
        form = BlogArticleForm()

    return render(request, 'article/create_article.html', {'form': form})




def edit_blog_article(request, id):
    article = get_object_or_404(BlogArticle, id=id)

    if request.method == 'POST':
        form = BlogArticleForm(request.POST)
        if form.is_valid():
            article.title = form.cleaned_data['title']
            article.date_published = form.cleaned_data['date_published']
            article.tag = form.cleaned_data['tag']
            article.content = form.cleaned_data['content']
            article.save()
            return redirect('blog-articles')  # Redirect to article list after successful update
    else:
        form = BlogArticleForm(initial={
            'title': article.title,
            'date_published': article.date_published,
            'tag': article.tag,
            'content': article.content,
        })

    return render(request, 'article/edit_blog_article.html', {'form': form})
