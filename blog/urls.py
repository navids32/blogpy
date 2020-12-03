from  django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('contact/', views.ContactPage.as_view(), name='contact'),
    url(r'^article/all/$', views.AllArticleAPIView.as_view(), name='all_articles'),

]