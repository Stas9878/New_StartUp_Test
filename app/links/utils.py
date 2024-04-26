from .models import Links
from urllib.parse import urlsplit
from datetime import datetime
import string, random


CHARS = string.ascii_letters


def _encode_url(url: str) -> str:
    code = ''.join(random.choice(CHARS) for _ in range(8))
    domain = urlsplit(url).netloc
    return {
        'url': f'{domain}/{code}',
        'code': code
    }
    

def get_encode_url(user, old_url: str) -> str:
    url = Links.objects.filter(old_url=old_url).first()
    
    if url:
        url.last_access = datetime.now()
        url.save()
        return url.new_url
    
    new_data_url = _encode_url(old_url)
    new_url = new_data_url['url']
    
    Links.objects.create(
        code=new_data_url['code'].lower(),
        old_url=old_url,
        new_url=new_url,
        user=user if user.is_authenticated else None
    )

    return new_url


def get_decode_url(new_url: str):
    pass