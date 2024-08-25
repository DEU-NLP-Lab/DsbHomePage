from django.urls import path
from . import views

urlpatterns = [
    # 이 부분에 url 패턴 넣기
    path('<int:pk>/', views.post_page),
    path('', views.posts_list),
]
