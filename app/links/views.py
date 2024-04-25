from django.http import HttpResponse
from django.shortcuts import render

def index_route(request) -> HttpResponse:
    return render(request, 'links/index.html')
