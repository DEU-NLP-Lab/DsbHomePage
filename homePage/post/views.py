from django.shortcuts import render
from .models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-pk')
    print(posts)

    return render(
        request,
        'post/index.html',
        {
            'posts': posts
        },
    )
