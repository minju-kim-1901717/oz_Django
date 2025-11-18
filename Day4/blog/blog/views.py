from http.client import responses

from django.contrib.auth.decorators import login_required
from django.contrib.sites import requests
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from blog.models import Blog
from blog.forms import BlogForm
from django.views.decorators.http import require_http_methods


def blog_list(request):
    #최신순으로 정렬
    blogs = Blog.objects.all().order_by('-created')

    #검색 <- 항상 페이지네이션 위로
    q = request.GET.get('q')
    if q:
        # 제목이랑 글 내용중에서 전체검색
        # blogs = blogs.filter(
        #     Q(title__icontains=q) |
        #     Q(content__icontains=q) |
        # )
        blogs = blogs.filter(title__icontains=q)

    #페이지네이션
    paginator = Paginator(blogs, 10)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    visits = int(request.COOKIES.get('visits', 0)) + 1

    request.session['count'] = request.session.get('count', 0) + 1

    context = {
        # 'blogs':blogs,
        'count':request.session['count'],
        'page_obj':page_obj,
    }

    responses = render(request, 'blog_list.html', context)
    responses.set_cookie('visits', visits)

    return responses


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {'todo':blog}
    return render(request, 'blog_detail.html',context)

@login_required()
def blog_create(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        blog = form.save(commit=False)
        blog.author = request.user
        blog.save()
        return redirect(reverse('blog_detail', kwargs={'pk':blog.pk}))

    form = BlogForm()

    context = {'form':form}
    return render(request,'blog_create.html',context)

@login_required()
def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk, author=request.user)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        blog = form.save()
        return redirect(reverse('blog_detail', kwargs={'pk':blog.pk}))

    context = {
        'todo':blog,
        'form':form,
    }
    return render(request,'blog_update.html',context)

@login_required()
@require_http_methods(['POST']) #이게 들어가면 밑에 주석부분 필요 없음
def blog_delete(request, pk):
    # if request.method != 'POST':
    #     raise Http404

    blog = get_object_or_404(Blog, pk=pk, author=request.user)
    blog.delete()
    return redirect(reverse('blog_list'))

