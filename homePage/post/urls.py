from django.urls import path
from post import views
from .views import download_post_file

urlpatterns = [
    # 이 부분에 url 패턴 넣기
    path('<int:pk>/', views.single_post_page),
    path('', views.index),
    path('posts/', views.posts),
    path('download/post/<int:post_id>/', download_post_file, name='download-post-file'),
]
