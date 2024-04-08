from django.shortcuts import render
from django.views.generic.base import View
from .models import Post


class PostView(View):
    '''Вывод записи на главный экран'''
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'Blog/main_screen.html', {'post_list': posts})

class PostDetail(View):
    '''Отдельная страница записи'''
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog/post_detail.html', {'post' : post})