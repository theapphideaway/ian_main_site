from django import forms
from blog_api.models import BlogArticle


class BlogArticleForm(forms.Form):
    title = forms.CharField(max_length=200)
    date_published = forms.CharField(max_length=200)
    tag = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)
