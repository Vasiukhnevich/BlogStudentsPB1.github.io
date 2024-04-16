from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import login, authenticate



class PostView(View):
    '''Вывод записи на главный экран'''
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'Blog/main_screen.html', {'post_list': posts})

class PostDetail(View):
    '''Отдельная страница записи'''
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'Blog/post_detail.html', {'post': post})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('')  # Замените 'home' на ваш URL-шаблон домашней страницы
    else:
        form = UserRegistrationForm()
    return render(request, 'Blog/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('')  # Замените 'home' на ваш URL-шаблон домашней страницы
            else:
                # Обработка ошибки входа
                pass
    else:
        form = UserLoginForm()
    return render(request, 'Blog/login.html', {'form': form})

