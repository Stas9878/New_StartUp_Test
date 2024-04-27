from django.test import TestCase
from rest_framework import serializers
from links.models import Links


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ['new_url', 'old_url', 'created_at']
