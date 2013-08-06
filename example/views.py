from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    context = {
        'brand_name': 'connexionSW',
        'brand_url': '#',
        'page_title': 'Index',
        'page_header': 'Initial Landing',
        'page_header_sub': 'page',
    }

    return render_to_response(
        'example/index.html',
        context,
        context_instance=RequestContext(request)
    )
