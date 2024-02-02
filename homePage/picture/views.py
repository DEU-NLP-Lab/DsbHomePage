from django.shortcuts import render

from .models import Picture


# Create your views here.
def picture_post(request):
    picture = Picture.objects.all().order_by('-pk')

    return render(
        request,
        'picture/picture_post.html',
        {
            'posts': picture
        },
    )