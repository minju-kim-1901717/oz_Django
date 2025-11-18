from http.client import responses

from django.contrib.sites import requests
from django.shortcuts import render, get_object_or_404

from blog.models import Blog


def blog_list(request):
    blogs = Blog.objects.all()

    visits = int(request.COOKIES.get('visits', 0)) + 1

    request.session['count'] = request.session.get('count', 0) + 1

    context = {
        'blogs':blogs,
        'count':request.session['count'],
    }

    responses = render(request, 'blog_list.html', context)
    responses.set_cookie('visits', visits)

    return responses


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {'blog':blog}
    return render(request, 'blog_detail.html',context)