from django.shortcuts import render
from django.views.generic.base import View
from .models import Post

"""Вывод записи на главный экран"""
class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'Blog/main_screen.html', {'post_list': posts})