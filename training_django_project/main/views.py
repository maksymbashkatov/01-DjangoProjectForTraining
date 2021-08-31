from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse('<h4>Main page test.</h4>')
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')