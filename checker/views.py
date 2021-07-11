from django.shortcuts import render
from django.template.loader import render_to_string
import requests
from .models import Url
from django.http import JsonResponse, HttpResponse
from .forms import UrlsForm
from .utils import get_code

# Create your views here.
def main(request):
    form = UrlsForm()
    return render(request, 'checker/main.html',context={'form':form})

def urls_create(request):
    if request.is_ajax():
        data = {'success': False, 'message':'Error'}
        urls = request.POST.get('urls', None)
        created_urls = list(Url.objects.values_list('address',flat=True))
        create_list = []
        if urls is not None:
            urls_list = urls.split(',')
            for url in urls_list:
                if url not in created_urls:
                    create_list.append(Url(address=url, status=get_code(url)))
            Url.objects.bulk_create(create_list)
            data = {'success': True, 'message':'Urls created'}
        return JsonResponse(data)

def urls_list(request):
    if request.is_ajax():
        context = {'success': False, 'user':'not authenticated'}
        if request.user.is_authenticated:
            urls = Url.objects.all()
            context = {'urls': urls}
        html = render_to_string('checker/url_list.html', context)
        return HttpResponse(html)