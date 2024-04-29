from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import NotAuthenticated, NotFound
from rest_framework.views import APIView
from links.models import Links
from .serializers import LinksSerializer
from links.utils import get_encode_url, get_decode_url


class LinkAPIView(APIView):
    def get(self, request) -> Response:
        if request.user.is_authenticated:
            links = Links.objects.filter(user=request.user)
            return Response({'links': LinksSerializer(links, many=True).data})
        raise NotAuthenticated()


class CreateLinkAPIView(APIView):
    def post(self, request) -> Response:
        target_url = request.data['old_url']
        encode_url = get_encode_url(request.user, target_url)
        new_url = Links.objects.get(new_url=encode_url)            
        return Response({'link': LinksSerializer(new_url).data})
    

class DecodeLinkAPIView(APIView):
    def post(self, request) -> Response:
        target_url = request.data['new_url']
        old_url = get_decode_url(target_url)  
        if old_url:     
            return Response({'link': LinksSerializer(old_url).data})
        raise NotFound(code=404, detail='Ссылка не найдена или вы ввели некорректоное значение')