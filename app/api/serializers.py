from rest_framework import serializers


class LinksSerializer(serializers.Serializer):
    new_url = serializers.CharField()
    old_url = serializers.URLField(max_length=1000)
    created_at = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')
