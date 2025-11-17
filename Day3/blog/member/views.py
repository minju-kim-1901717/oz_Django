from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login



def signup(request):
    # username = request.POST.get('username')
    # password1 = request.POST['password1']
    # password2 = request.POST['password2']

    #user 중복확인
    #PW 두개가 맞는지, 정책이 올바른지

    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(settings.LOGIN_URL)

    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/accounts/login/')
    # else:
    #     form = UserCreationForm()

    context = {'form':form}

    return render(request,'registration/signup.html',context)

def login(request):
    form = AuthenticationForm(request, request.POST or None)
    if form.is_valid():
        django_login(request, form.get_user())
        return redirect('/')
    context = {'form':form}

    return render(request, 'registration/login.html', context)