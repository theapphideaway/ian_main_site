from rest_framework import generics
from .models import BlogArticle
from .serializers import BlogArticleSerializer
from rest_framework.permissions import IsAuthenticated


class BlogList(generics.ListAPIView):
    queryset = BlogArticle.objects.all()
    serializer_class = BlogArticleSerializer


class BlogDetail(generics.RetrieveAPIView):
    queryset = BlogArticle.objects.all()
    serializer_class = BlogArticleSerializer
    lookup_field = 'id'


class BlogArticleCreateView(generics.CreateAPIView):
    queryset = BlogArticle.objects.all()
    serializer_class = BlogArticleSerializer

