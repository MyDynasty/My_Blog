# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Article,Tag,Category
import markdown

def index(request):
    category_list = Category.objects.all()
    tag_list = Tag.objects.all()
    total = Article.objects.order_by('-id')[:1][0].id
    article_list = Article.objects.order_by('-date_time')
    template = loader.get_template('index.html')
    context = {
        'article_list': article_list,
        'category_list': category_list,
        'tag_list': tag_list,
        'total': total
    }
    return HttpResponse(template.render(context, request))
    #return render(request,'index.html')

def test(request):
    return render(request, 'blog/1.html')

def articles(request, article_id):
    category_list = Category.objects.all()
    tag_list = Tag.objects.all()
    article = Article.objects.get(id=article_id)
    template = loader.get_template('article.html')
    article.content = markdown.markdown(article.content,
                                        extensions=[
                                            'markdown.extensions.extra',
                                            'markdown.extensions.codehilite',
                                            'markdown.extensions.toc',
                                        ])
    context = {
        'article':article,
        'category_list': category_list,
        'tag_list': tag_list,
    }
    return HttpResponse(template.render(context, request))