from django.db import models
from django.contrib.auth import get_user_model


class Links(models.Model):
    code = models.CharField(max_length=8, unique=True, db_index=True, default='qwertyui')
    old_url = models.URLField(max_length=1000)
    new_url = models.CharField(max_length=100, unique=True, db_index=True)
    user = models.ForeignKey(get_user_model(), null=True, blank=True,  on_delete=models.CASCADE, related_name='links', db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_access = models.DateTimeField(max_length=500, auto_now=True)

    class Meta:
        verbose_name = 'Ссылку'
        verbose_name_plural = 'Ссылки'