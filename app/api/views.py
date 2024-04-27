from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import NotAuthenticated
from rest_framework.views import APIView
from links.models import Links
from .serializers import LinksSerializer, CreateLinksSerializer
from links.utils import get_encode_url


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
        return Response({'link': CreateLinksSerializer(new_url).data})