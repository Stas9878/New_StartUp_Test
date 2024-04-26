from django.db import models
from django.contrib.auth import get_user_model

class Links(models.Model):
    old_url = models.URLField(max_length=1000)
    new_url = models.CharField(max_length=100, unique=True, db_index=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='links')
    created_at = models.DateTimeField(auto_now_add=True)
    last_access = models.DateTimeField(max_length=500, auto_now=True)
