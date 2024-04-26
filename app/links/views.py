from django.http import HttpResponse
from django.shortcuts import render
from .forms import TinyUrlForm


def index_route(request) -> HttpResponse:
    if request.method == 'POST':
        form = TinyUrlForm(request.POST)

        if form.is_valid():
            target_url = form.data['target_url']
            print(target_url)
            pass
    else:
        form = TinyUrlForm()
        
    return render(request, 'links/index.html', {'form': form})
