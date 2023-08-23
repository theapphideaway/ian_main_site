from django.urls import path
from . import views

app_name = 'blog_site'

urlpatterns = [
    path('', views.home, name='home'),
    path('contributions/', views.contributions, name='contributions'),
    path('blog/', views.blog, name='blog'),
    path('blog/article/<int:article_id>/', views.article_details, name='article_details'),

]
