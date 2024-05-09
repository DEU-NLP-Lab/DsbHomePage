from django.shortcuts import render

from .models import Picture


# Create your views here.
def picture_post(request):
    picture = Picture.objects.all().order_by('-pk')

    form_link = read_form_link()

    return render(
        request,
        'picture/picture_post.html',
        {
            'pictures': picture,
            'form_link': form_link
        },
    )


def picture_detail_page(request, pk):
    picture = Picture.objects.get(pk=pk)

    form_link = read_form_link()

    return render(
        request,
        'picture/picture_detail_page.html',
        {
            'picture': picture,
            'form_link': form_link
        },
    )


def read_form_link():
    with open('linkSetting/form.txt', 'r', encoding="utf-8") as file:
        url = file.read().split('\n')[-1].strip()

    return url
