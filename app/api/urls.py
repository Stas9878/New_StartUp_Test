from django.urls import path, include
from api.views import LinkAPIView, CreateLinkAPIView, DecodeLinkAPIView


app_name = 'apiv1'


urlpatterns = [
    path('user-links/', LinkAPIView.as_view(), name='links_list'),
    path('create-link/', CreateLinkAPIView.as_view(), name='create_link'),
    path('decode-url/', DecodeLinkAPIView.as_view(), name='decode_url'),
]