from http.client import responses

from django.contrib.auth.decorators import login_required
from django.contrib.sites import requests
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from todo.models import Todo
from todo.forms import TodoForm
from django.views.decorators.http import require_http_methods


def todo_list(request):
    #최신순으로 정렬
    todos = Todo.objects.all().order_by('-created')

    #검색 <- 항상 페이지네이션 위로
    q = request.GET.get('q')
    if q:
        todos = todos.filter(title__icontains=q)

    #페이지네이션
    paginator = Paginator(todos, 10)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    visits = int(request.COOKIES.get('visits', 0)) + 1

    request.session['count'] = request.session.get('count', 0) + 1

    context = {
        # 'todos':todos,
        'count':request.session['count'],
        'page_obj':page_obj,
    }

    responses = render(request, 'todo_list.html', context)
    responses.set_cookie('visits', visits)

    return responses


def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    context = {'todo':todo}
    return render(request, 'todo_detail.html',context)

@login_required()
def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.author = request.user
        todo.save()
        return redirect(reverse('todo_detail', kwargs={'pk':todo.pk}))

    form = TodoForm()

    context = {'form':form}
    return render(request,'todo_create.html',context)

@login_required()
def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk, author=request.user)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        todo = form.save()
        return redirect(reverse('todo_detail', kwargs={'pk':todo.pk}))

    context = {
        'todo':todo,
        'form':form,
    }
    return render(request,'todo_update.html',context)

@login_required()
@require_http_methods(['POST']) #이게 들어가면 밑에 주석부분 필요 없음
def todo_delete(request, pk):
    # if request.method != 'POST':
    #     raise Http404

    todo = get_object_or_404(Todo, pk=pk, author=request.user)
    todo.delete()
    return redirect(reverse('todo_list'))

