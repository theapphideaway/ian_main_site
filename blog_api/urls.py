from django.urls import path
from .views import BlogList, BlogDetail

app_name = 'blog_api'

urlpatterns = [
    path('blog/all/', BlogList.as_view(), name='blog-articles'),
    path('blog/<int:id>/', BlogDetail.as_view(), name='blog-detail'),
]
