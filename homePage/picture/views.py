from django.shortcuts import render

from .models import Picture


# Create your views here.
def picture_post(request):
    picture = Picture.objects.all().order_by('-pk')

    return render(
        request,
        'picture/picture_post.html',
        {
            'pictures': picture
        },
    )


def picture_detail_page(request, pk):
    picture = Picture.objects.get(pk=pk)

    return render(
        request,
        'picture/picture_detail_page.html',
        {
            'picture': picture
        },
    )
