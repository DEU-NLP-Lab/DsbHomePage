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
