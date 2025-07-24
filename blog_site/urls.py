from django.urls import path
from . import views

app_name = 'blog_site'

urlpatterns = [
    path('', views.home, name='home'),
    path('experience/', views.experience, name='experience'),
    path('blog/', views.blog, name='blog'),
    path('blog/article/<int:article_id>/', views.article_details, name='article_details'),
    path('add231AsAX13SSDcCSDFSDCBVSdC/', views.add_blog_article, name='add'),
    path('edit-blog/<int:id>/', views.edit_blog_article, name='edit-blog'),
    path('math-test', views.math_test, name='math-test'),
]
