from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
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