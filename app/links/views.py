from django.http import HttpResponse
from django.shortcuts import render
from .forms import TinyUrlForm
from .utils import get_decode_url, get_encode_url


def index_route(request) -> HttpResponse:
    if request.method == 'POST':
        form = TinyUrlForm(request.POST)

        if form.is_valid():
            target_url = form.data['target_url']
            encode_url = get_encode_url(request.user, target_url)
            return render(request, 'links/index.html', {
                'form': form, 
                'encode_url': encode_url,
                'target_url': target_url,
            }) 
    else:
        form = TinyUrlForm()
        
    return render(request, 'links/index.html', {'form': form})
