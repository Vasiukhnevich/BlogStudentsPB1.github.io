from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm

# Create your views here.

def posts(request):
    posts = Articles.objects.order_by('date')
    return render(request, 'news/all_posts.html', {'posts': posts})

def create(request):
    error = ''
    if request .method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
        else:
            error = 'неверная форма'


    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)

