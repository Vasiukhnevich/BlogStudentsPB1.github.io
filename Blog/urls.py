from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.PostView.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),

    # URL для страницы регистрации
    path('register/', views.register, name='register'),

    # URL для страницы входа (используем встроенное представление)
    path('login/', LoginView.as_view(template_name='Blog/login.html'), name='login'),

    # URL для страницы выхода (используем встроенное представление)
    path('logout/', LogoutView.as_view(), name='logout'),

]