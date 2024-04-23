from django.urls import path
from . import views

urlpatterns = [
    # 이 부분에 url 패턴 넣기
    path('<int:pk>/', views.single_post_page),
    path('', views.index),
    path('posts/', views.posts),
]
