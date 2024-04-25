from django.urls import path
from .views import index_route


app_name = 'links'


urlpatterns = [
    path('', index_route, name='index'),
]