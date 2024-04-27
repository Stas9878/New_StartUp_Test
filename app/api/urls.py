from django.urls import path
from api.views import LinkAPIView, CreateLinkAPIView


app_name = 'apiv1'


urlpatterns = [
    path('user-links/', LinkAPIView.as_view(), name='links_list'),
    path('create-link/', CreateLinkAPIView.as_view(), name='create_link'),
]