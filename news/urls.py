from django.urls import path
from . import views


urlpatterns = [
    path('', views.posts, name='posts'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.PostDetailView.as_view(), name='news-detail')
]