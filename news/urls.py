from django.urls import path
from . import views


urlpatterns = [
    path('', views.posts, name='posts'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.PostDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='news-delete')
]