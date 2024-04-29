from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import NotAuthenticated, NotFound
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from links.models import Links
from .serializers import LinksSerializer
from links.utils import get_encode_url, get_decode_url


class LinkAPIView(APIView):
    @swagger_auto_schema(responses={'200': LinksSerializer(many=True)})
    def get(self, request) -> Response:
        if request.user.is_authenticated:
            links = Links.objects.filter(user=request.user)
            return Response({'links': LinksSerializer(links, many=True).data})
        raise NotAuthenticated()


class CreateLinkAPIView(APIView):
    params = openapi.Parameter('url', openapi.IN_HEADER, description="Введите url который хотите сократить", type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[params], responses={'200': LinksSerializer})
    def post(self, request) -> Response:
        target_url = request.headers['url']
        encode_url = get_encode_url(request.user, target_url)
        new_url = Links.objects.get(new_url=encode_url)            
        return Response(LinksSerializer(new_url).data, status=status.HTTP_201_CREATED)
    

class DecodeLinkAPIView(APIView):
    params = openapi.Parameter('url', openapi.IN_HEADER, description="Введите url который нужно декодировать", type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[params], responses={'200': LinksSerializer})
    def post(self, request) -> Response:
        target_url = request.headers['url']
        old_url = get_decode_url(target_url)  
        if old_url:     
            return Response(LinksSerializer(old_url).data, status=status.HTTP_200_OK)
        raise NotFound(code=status.HTTP_400_BAD_REQUEST, detail='Ссылка не найдена или вы ввели некорректоное значение')