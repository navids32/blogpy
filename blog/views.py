from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class IndexPage(TemplateView):

    def get(self, request, **kwargs):
        article_data = []
        all_articles = Article.objects.all().order_by('-create_at')[:9]

        for article in all_articles:
            article_data.append({
                'title' : article.title,
                'cover' : article.cover.url,
                'category' : article.category.title,
                'create_at' : article.create_at.date(),
            })

        promote_data = []
        all_promote_articles = Article.objects.filter(promote=True)
        for promote_article in all_promote_articles:
            promote_data.append({
                'title': promote_article.title,
                'avatar': promote_article.author.avatar.url if promote_article.author.avatar else None,
                'category': promote_article.category.title,
                'author': promote_article.author.user.first_name + ' ' +promote_article.author.user.last_name,
                'cover': promote_article.cover.url if promote_article.cover else None,
                'create_at': promote_article.create_at.date(),
            })


        context = {
            'article_data' : article_data,
            'promote_article_data' : promote_data,
        }

        return render(request, 'index.html', context)

class ContactPage(TemplateView):
    template_name = 'page-contact.html'



class AllArticleAPIView(APIView):

    def get(self, requset, format=None):
        try:
            all_articles = Article.objects.all().order_by('-create_at')[:9]
            data = []
            for article in all_articles:
                data.append({
                    'title': article.title,
                    'cover': article.cover.url if article.cover else None,
                    'content': article.content,
                    'create_at':article.create_at,
                    'category': article.category.title,
                    'author': article.author.user.first_name +" "+ article.author.user.last_name,
                    'promote': article.promote,
                })
            return Response({'data': data}, status=status.HTTP_200_OK)

        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)