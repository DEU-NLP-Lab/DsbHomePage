from django.shortcuts import render

from .models import Results


# Create your views here.
def results_post(request):
    results = Results.objects.all().order_by('-pk')

    return render(
        request,
        'results_post.html',
        {
            'results': results,
        },
    )


def results_detail_page(request, pk):
    result = Results.objects.get(pk=pk)

    return render(
        request,
        'results_detail_page.html',
        {
            'result': result,
        },
    )
