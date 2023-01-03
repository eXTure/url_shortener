from django.db import models


class Url(models.Model):
    full_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=16, unique=True)
    is_active = models.BooleanField(default=True)
    clicks = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_url
