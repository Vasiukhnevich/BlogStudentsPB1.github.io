from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
# Create your views here.

def posts(request):
    posts = Articles.objects.order_by('-date')
    return render(request, 'news/all_posts.html', {'posts': posts})

class PostUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm

class PostDeleteView(DeleteView):
    model = Articles
    template_name = 'news/news-delete.html'
    success_url = '/posts'



class PostDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

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

