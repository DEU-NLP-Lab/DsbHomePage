from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-pk')[:10]

    return render(
        request,
        'post/index.html',
        {
            'posts': posts
        },
    )


def posts(request):

    post_list = Post.objects.all().order_by('-pk')  # or however you want to order them
    paginator = Paginator(post_list, 20)  # 20 posts per page

    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
    }

    return render(
        request,
        'post/posts.html',
        {
            'posts': page_obj,
        }
    )


def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'post/postDetail.html',
        {
            'post': post,
        }
    )
