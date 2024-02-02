from django.urls import path
from . import views

urlpatterns = [
    # 이 부분에 url 패턴 넣기
    path('<int:pk>/', views.picture_detail_page),
    path('', views.picture_post),
]
