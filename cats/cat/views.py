from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from cat.forms import Catforms
from cat.models import Cat
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
    """Вывод домашней страницы"""
    if request.user.is_authenticated:
        user = request.user
        objects = Cat.objects.filter(User=user)

    return render(request, 'index.html',locals())

def registration(request):
    '''Регистрация нового пользователя'''

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            form.save()
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')

    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, 'registration/registration.html', context)

@login_required
def create_cat(request):
    """Создание кота"""
    if request.method == 'GET':
        form = Catforms(initial={'User': request.user})
    else:
        form = Catforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form': form}
    return render(request, 'create_cat.html',context)


@login_required
def cat_view(request,cat_id):
    '''Просмотр кота'''
    cat = Cat.objects.get(pk=cat_id)
    if cat.User == request.user:
        context = {'cat': cat}
    else:
        context = {'error' : 'Ошибка. Вы пытаетесь посмотреть чужого кота.'}

    return render(request,'cat_view.html',context)

@login_required
def cat_change(request,cat_id):
    '''Изменение кота'''
    cat = Cat.objects.get(pk=cat_id)
    if cat.User == request.user:
        if request.method == 'GET':
            cat = Catforms(instance=cat)
            context = {'cat': cat}

        if request.method == 'POST':
            form = Catforms(instance=cat, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')

    else:
        context = {'error': 'Ошибка. Вы пытаетесь изменить чужого кота.'}


    return render(request, 'cat_change.html', context)