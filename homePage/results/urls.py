from django.urls import path
from . import views

urlpatterns = [
    # 이 부분에 url 패턴 넣기
    path('', views.results_post)
]
