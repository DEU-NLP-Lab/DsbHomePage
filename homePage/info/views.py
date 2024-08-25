import os
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Info


# Create your views here.

def posts_list(request):
    post_list = Info.objects.all().order_by('-pk')  # or however you want to order them
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
        'info/posts.html',
        {
            'posts': page_obj,
        }
    )


def post_page(request, pk):
    post = Info.objects.get(pk=pk)

    return render(
        request,
        'info/postDetail.html',
        {
            'post': post,
        }
    )
