from django.urls import path
from . import views


urlpatterns = [
    path('', views.posts, name='posts'),
    path('create', views.create, name='create'),
]